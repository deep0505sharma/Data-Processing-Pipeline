
import pandas as pd
import numpy as np

def remove_outliers(df: pd.DataFrame, method: str = "iqr", threshold: float = 3.0) -> pd.DataFrame:
    """
    Remove outliers from numerical columns using IQR or Z-score.

    Parameters
    ----------
    df : DataFrame
        Input data.
    method : str
        "iqr" or "zscore".
    z_threshold : float
        Threshold for z-score filtering.

    Returns
    -------
    DataFrame
        DataFrame with outliers removed.
    """

    numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns
    df_clean = df.copy()

    if method == "iqr":
        print("Applying IQR outlier removal...")
        for col in numeric_cols:
            Q1 = df_clean[col].quantile(0.25)
            Q3 = df_clean[col].quantile(0.75)
            IQR = Q3 - Q1
            lower = Q1 - 1.5 * IQR
            upper = Q3 + 1.5 * IQR
            df_clean = df_clean[(df_clean[col] >= lower) & (df_clean[col] <= upper)]

    elif method == "zscore":
        print("Applying Z-score outlier removal...")
        for col in numeric_cols:
            col_mean = df_clean[col].mean()
            col_std = df_clean[col].std()
            if col_std == 0:
                continue
            z_scores = (df_clean[col] - col_mean) / col_std
            df_clean = df_clean[z_scores.abs() <= threshold]

    else:
        raise ValueError("Invalid method. Choose 'iqr' or 'zscore'.")

    return df_clean
