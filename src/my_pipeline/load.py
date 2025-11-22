from pathlib import Path
import pandas as pd

def save_data(df: pd.DataFrame, output_path: str) -> None:
    """Load processed data to CSV output."""
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    df.to_csv(output_path, index=False)
