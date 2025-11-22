import pandas as pd
from pathlib import Path

def extract_data(input_path: str) -> pd.DataFrame:
    """Extract raw data from a CSV file."""
    file_path = Path(input_path)

    if not file_path.exists():
        raise FileNotFoundError(f"Input file does not exist: {file_path}")

    df = pd.read_csv(file_path)
    return df
