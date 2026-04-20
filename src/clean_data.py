import pandas as pd
from pathlib import Path

RAW_PATH = Path("data/raw/WA_Fn-UseC_-Telco-Customer-Churn.csv")
OUT_PATH = Path("data/processed/churn_cleaned.csv")

def main():
    df = pd.read_csv(RAW_PATH)

    print("Shape:", df.shape)
    print("\nColumns:\n", df.columns.tolist())
    print("\nMissing values:\n", df.isnull().sum())
    print("\nDuplicates:", df.duplicated().sum())

    # Convert TotalCharges to numeric
    df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")

    print("\nMissing TotalCharges after conversion:", df["TotalCharges"].isnull().sum())

    # Drop rows where TotalCharges is missing
    df = df.dropna(subset=["TotalCharges"]).copy()

    # Standardize text values if needed
    for col in df.select_dtypes(include="object").columns:
        df[col] = df[col].astype(str).str.strip()

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUT_PATH, index=False)

    print("\nCleaned file saved to:", OUT_PATH)
    print("Final shape:", df.shape)

if __name__ == "__main__":
    main()