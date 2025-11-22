import pandas as pd
from sklearn.preprocessing import OneHotEncoder, LabelEncoder


def encode_onehot(df):
    cat_cols = df.select_dtypes(include=["object", "category"]).columns.tolist()
    if not cat_cols:
        print("No categorical columns found. Skipping one-hot encoding.")
        return df
    print(f"One-Hot Encoding: {cat_cols}")
    return pd.get_dummies(df, columns=cat_cols, drop_first=False)


def encode_label(df):
    cat_cols = df.select_dtypes(include=["object", "category"]).columns.tolist()
    if not cat_cols:
        print("No categorical columns found. Skipping label encoding.")
        return df

    print(f"Label Encoding: {cat_cols}")
    df = df.copy()
    for col in cat_cols:
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col].astype(str))
    return df


def encode_target(df, target_column):
    """
    Target encoding: replace categories with mean(target) for each category.

    Example: if target = "price":
        brand=A → 100
        brand=B → 130
    """

    if target_column not in df.columns:
        raise ValueError(f"Target column '{target_column}' not found in DataFrame.")

    cat_cols = df.select_dtypes(include=["object", "category"]).columns.tolist()
    if not cat_cols:
        print("No categorical columns found. Skipping target encoding.")
        return df

    df = df.copy()

    for col in cat_cols:
        print(f"Target Encoding {col} using target '{target_column}'")

        means = df.groupby(col)[target_column].mean()
        df[col] = df[col].map(means)

    return df


def encode_categorical(df, method="label", target_column=None):
    """
    Wrapper to call encoding methods.
    """

    if method == "onehot":
        return encode_onehot(df)
    elif method == "label":
        return encode_label(df)
    elif method == "target":
        if target_column is None:
            raise ValueError("Target encoding requires --target-column")
        return encode_target(df, target_column)
    else:
        raise ValueError("Invalid encoding method. Choose: onehot, label, target")

