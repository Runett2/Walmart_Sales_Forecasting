from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent
RAW_DATA_DIR = BASE_DIR / "data" / "raw"
PROCESSED_DATA_DIR = BASE_DIR / "data" / "processed"


def load_raw_data():
    train = pd.read_csv(RAW_DATA_DIR / "train.csv")
    test = pd.read_csv(RAW_DATA_DIR / "test.csv")
    features = pd.read_csv(RAW_DATA_DIR / "features.csv")
    stores = pd.read_csv(RAW_DATA_DIR / "stores.csv")

    return train, test, features, stores


def merge_datasets(sales_df, features_df, stores_df):
    df = sales_df.merge(
        features_df,
        on=["Store", "Date", "IsHoliday"],
        how="left"
    )

    df = df.merge(
        stores_df,
        on="Store",
        how="left"
    )

    return df


def load_train_data():
    train, _, features, stores = load_raw_data()
    return merge_datasets(train, features, stores)


def load_test_data():
    _, test, features, stores = load_raw_data()
    return merge_datasets(test, features, stores)


def save_processed_data(df: pd.DataFrame, filename: str):
    PROCESSED_DATA_DIR.mkdir(parents=True, exist_ok=True)
    df.to_csv(PROCESSED_DATA_DIR / filename, index=False)