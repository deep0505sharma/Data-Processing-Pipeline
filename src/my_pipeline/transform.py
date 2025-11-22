import pandas as pd

def handle_missing_values(df: pd.DataFrame,method: str = "drop",fill_value=None) -> pd.DataFrame:
    """
    Handle missing values using various strategies.

    Parameters
    ----------
    df : DataFrame
        Input data.
    method : str
        One of:
            - "drop"
            - "mean"
            - "median"
            - "mode"
            - "constant"
            - "ffill"
            - "bfill"
    fill_value : Any
        Required when method="constant".

    Returns
    -------
    DataFrame
        DataFrame with missing values handled.
    """

    df_clean = df.copy()

    if method == "drop":
        print("Dropping rows with missing values...")
        return df_clean.dropna()

    elif method == "mean":
        print("Filling missing numeric values with mean...")
        return df_clean.fillna(df_clean.mean(numeric_only=True))

    elif method == "median":
        print("Filling missing numeric values with median...")
        return df_clean.fillna(df_clean.median(numeric_only=True))

    elif method == "mode":
        print("Filling missing values with mode...")
        for col in df_clean.columns:
            if not df_clean[col].isna().sum():
                continue
            mode_value = df_clean[col].mode(dropna=True)
            if not mode_value.empty:
                df_clean[col] = df_clean[col].fillna(mode_value.iloc[0])
        return df_clean

    elif method == "constant":
        if fill_value is None:
            raise ValueError("You must specify fill_value when using method='constant'")
        print(f"Filling missing values with constant value: {fill_value}")
        return df_clean.fillna(fill_value)

    elif method == "ffill":
        print("Forward-filling missing values...")
        return df_clean.ffill()

    elif method == "bfill":
        print("Backward-filling missing values...")
        return df_clean.bfill()

    else:
        raise ValueError(
            "Invalid method. Choose from: drop, mean, median, mode, constant, ffill, bfill"
        )


def transform_data(df: pd.DataFrame, method: str = "drop", fill_value=None) -> pd.DataFrame:
    """
    Apply transformations including missing value handling.

    Parameters
    ----------
    df : DataFrame
        Raw dataframe.
    missing_method : str
        Missing-value handling strategy.
    fill_value : Any
        Used only for constant fill method.

    Returns
    -------
    DataFrame
        Transformed dataframe.
    """

    print("Running transform step...")

    df = handle_missing_values(df, method=method, fill_value=fill_value)

    print("✔ Missing value handling done")
    return df

