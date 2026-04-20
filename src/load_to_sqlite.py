import pandas as pd
import sqlite3
from pathlib import Path

CSV_PATH = Path("data/processed/churn_cleaned.csv")
DB_PATH = Path("data/processed/churn.db")

def main():
    df = pd.read_csv(CSV_PATH)
    conn = sqlite3.connect(DB_PATH)
    df.to_sql("churn_data", conn, if_exists="replace", index=False)
    conn.close()
    print("Loaded data into SQLite DB:", DB_PATH)

if __name__ == "__main__":
    main()