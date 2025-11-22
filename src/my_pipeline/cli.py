import click
import tomllib
from pathlib import Path
import os
import toml

from .extract import extract_data
from .transform import transform_data
from .outliers import remove_outliers
from .normalize import normalize_data
from .encode import encode_categorical
from .load import save_data
from .logger import get_logger
from .profiler import profile_step
from tqdm import tqdm
import time

logger = get_logger("PipelineCLI")

# -------------------------------------------------------------
# Helper: Simulate progress bar for long steps
# -------------------------------------------------------------
def slow_loop_sim(label: str, seconds: float = 2.0):
    with click.progressbar(range(100), label=label) as bar:
        for _ in bar:
            time.sleep(seconds / 100)

# -------------------------------------------------------------
# Helper: Load TOML config
# -------------------------------------------------------------
def load_config(config_path):
    config_file = Path(config_path)
    if not config_file.exists():
        raise FileNotFoundError(f"Config file not found: {config_path}")

    with open(config_file, "rb") as f:
        return tomllib.load(f)


# -------------------------------------------------------------
# Helper: Merge CLI params with config values
# CLI > Config > Default
# -------------------------------------------------------------
def merge_params(cli_params, config):
    merged = {}

    # STEP ORDER
    merged["steps"] = cli_params.get("steps") or config.get("steps", [])

    # EXTRACT
    merged["input_path"] = cli_params.get("input_path") or config["extract"].get("input_path")

    # LOAD
    merged["output_path"] = cli_params.get("output_path") or config["load"].get("output_path")

    # TRANSFORM
    tr_cfg = config.get("transform", {})
    merged["missing_method"] = cli_params.get("missing_method") or tr_cfg.get("method")
    merged["fill_value"] = cli_params.get("fill_value") or tr_cfg.get("fill_value")

    # OUTLIERS
    o_cfg = config.get("outliers", {})
    merged["outlier_method"] = cli_params.get("outlier_method") or o_cfg.get("method")
    merged["threshold"] = o_cfg.get("threshold", 1.5)

    # NORMALIZATION
    n_cfg = config.get("normalize", {})
    merged["normalize_method"] = cli_params.get("normalize_method") or n_cfg.get("method")

    # ENCODING
    e_cfg = config.get("encode", {})
    merged["encode_method"] = cli_params.get("encode_method") or e_cfg.get("method")
    merged["target_column"] = cli_params.get("target_column") or e_cfg.get("target_column")

    return merged


# -------------------------------------------------------------
# MAIN RUN COMMAND
# -------------------------------------------------------------
@click.group()
def cli():
    pass


@cli.command()
@click.argument("input_path", required=False)
@click.argument("output_path", required=False)
@click.option("--config", "-c", help="Path to settings.toml")
@click.option("--steps", multiple=True, type=str, help="Pipeline steps to run")
@click.option("--missing-method", type=click.Choice(["drop", "mean", "median", "mode", "constant", "ffill", "bfill"]))
@click.option("--fill-value")
@click.option("--outlier-method", type=click.Choice(["iqr", "zscore"]))
@click.option("--normalize-method", default = "minmax", type=click.Choice(["minmax", "zscore", "robust"]))
@click.option("--encode-method", default="label", type=click.Choice(["onehot", "label", "target"]))
@click.option("--target-column", type=str, help="Required for target encoding")
@click.option("--threshold", default=1.5)
def run(input_path, output_path, config, steps,
        missing_method, fill_value, outlier_method, threshold,
        normalize_method, encode_method, target_column):
    """
    Run the data pipeline using CLI or config settings.toml
    """

    # --------------------------
    # Load config TOML
    # --------------------------
    if config:
        config_data = load_config(config)
        click.echo(f"Loaded config from {config}")
    else:
        config_data = {}

    # --------------------------
    # Merge config + CLI
    # --------------------------
    cli_params = {
        "input_path": input_path,
        "output_path": output_path,
        "steps": list(steps) if steps else None,
        "missing_method": missing_method,
        "fill_value": fill_value,
        "outlier_method": outlier_method,
        "normalize_method": normalize_method,
        "encode_method": encode_method,
        "target_column": target_column,
        "threshold": threshold  # default threshold
    }

    params = merge_params(cli_params, config_data)

    click.echo(f"Steps to run: {params['steps']}")

    df = None

    # ---------------------------------------------------------
    # Execute steps in order
    # ---------------------------------------------------------
    for step in params["steps"]:

        if step == "extract":
            slow_loop_sim("Extracting data…")
            df = profile_step("Extract data",extract_data,params["input_path"])

        elif step == "transform":
            if df is None:
                df = extract_data(params["input_path"])
            slow_loop_sim("Transforming data…")
            df = profile_step("Transform data",transform_data,df,
                                method=params["missing_method"],
                                fill_value=params["fill_value"])

        elif step == "outliers":
            if df is None:
                df = extract_data(params["input_path"])
            slow_loop_sim("Removing outliers…")
            df = profile_step("Remove Outliers",remove_outliers,df,
                         method=params["outlier_method"],
                         threshold=params["threshold"])

        elif step == "normalize":
            if df is None:
                df = extract_data(params["input_path"])
            slow_loop_sim("Normalizing data…")
            df = profile_step("Normalize data",normalize_data,df, method=params["normalize_method"])

        elif step == "encode":
            if df is None:
                df = extract_data(params["input_path"])
            slow_loop_sim("Encoding categorical variables…")
            df = profile_step("Categorical Encoding",encode_categorical,df,
                     method=params["encode_method"],
                     target_column=params["target_column"])

        elif step == "load":
            slow_loop_sim("Saving data…")
            save_data(df, params["output_path"])
            

    logger.info("Pipeline run completed!")

# -------------------------------------------------------------
# RUN ALL — full pipeline in fixed order
# -------------------------------------------------------------
@cli.command()
@click.argument("input_path", required=False)
@click.argument("output_path", required=False)
@click.option("--config", "-c", help="Path to settings.toml")
@click.option("--missing-method", type=click.Choice(["drop", "mean", "median", "mode", "constant", "ffill", "bfill"]))
@click.option("--fill-value")
@click.option("--outlier-method", type=click.Choice(["iqr", "zscore"]))
@click.option("--normalize-method", default = "minmax", type=click.Choice(["minmax", "zscore", "robust"]))
@click.option("--encode-method", default="label", type=click.Choice(["onehot", "label", "target"]))
@click.option("--target-column", type=str, help="Required for target encoding")
@click.option("--threshold", default=1.5)
def run_all(input_path, output_path, config,
            missing_method, fill_value, outlier_method,
            normalize_method, encode_method, target_column, threshold):
    """
    Run ALL pipeline steps in fixed order:
    extract → transform → outliers → normalize → encode → load
    """
    click.echo("Running FULL pipeline")

    # --------------------------
    # Load config if provided
    # --------------------------
    if config:
        config_data = load_config(config)
        click.echo(f"Loaded config from {config}")
    else:
        config_data = {}

    # --------------------------
    # Merge CLI overrides
    # --------------------------
    cli_params = {
        "input_path": input_path,
        "output_path": output_path,
        "missing_method": missing_method,
        "fill_value": fill_value,
        "outlier_method": outlier_method,
        "threshold": threshold,
        "normalize_method": normalize_method,
        "encode_method": encode_method,
        "target_column": target_column,
        "steps": None   # run-all ignores config steps
    }

    params = merge_params(cli_params, config_data)

    # --------------------------------------------
    # Execute steps (fixed order)
    # --------------------------------------------
    slow_loop_sim("Extracting…")
    df = profile_step("Extract data",extract_data,params["input_path"])

    slow_loop_sim("Transforming…")
    df = profile_step("Transform data",transform_data, df,
                                method=params["missing_method"],
                                fill_value=params["fill_value"])
    
    slow_loop_sim("Removing outliers…")
    df = profile_step("Remove Outliers",remove_outliers, df,
                         method=params["outlier_method"],
                         threshold=params["threshold"])

    slow_loop_sim("Normalizing…")
    df = profile_step("Normalize data",normalize_data,df, method=params["normalize_method"])

    slow_loop_sim("Encoding…")
    df = profile_step("Categorical Encoding",encode_categorical, df,
                     method=params["encode_method"],
                     target_column=params["target_column"])

    slow_loop_sim("Saving data…")
    save_data(df, params["output_path"])

    logger.info("Pipeline run-all completed!")



if __name__ == "__main__":
    cli()

