
import pandas as pd

def normalize_data(df: pd.DataFrame, method: str = "minmax") -> pd.DataFrame:
    """
    Normalize numerical columns in a DataFrame.

    Parameters
    ----------
    df : DataFrame
        Input data.
    method : str
        Options: "minmax", "zscore", "robust".

    Returns
    -------
    DataFrame
        Normalized DataFrame (not saved to disk).
    """

    numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns

    if len(numeric_cols) == 0:
        print("⚠ No numeric columns found to normalize.")
        return df

    df_norm = df.copy()

    if method == "minmax":
        print("Applying Min-Max Normalization...")
        for col in numeric_cols:
            df_norm[col] = (df[col] - df[col].min()) / (df[col].max() - df[col].min())

    elif method == "zscore":
        print("Applying Z-score Standardization...")
        for col in numeric_cols:
            df_norm[col] = (df[col] - df[col].mean()) / df[col].std()

    elif method == "robust":
        print("Applying Robust Scaling (less sensitive to outliers)...")
        for col in numeric_cols:
            median = df[col].median()
            iqr = df[col].quantile(0.75) - df[col].quantile(0.25)
            df_norm[col] = (df[col] - median) / iqr

    else:
        raise ValueError("Invalid method. Choose 'minmax', 'zscore', or 'robust'.")

    return df_norm
