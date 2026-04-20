# Advanced Churn Analytics & Retention Intelligence System

## Overview
This project builds an end-to-end customer churn analytics workflow on telecom customer data using **Python, SQLite, SQL, and Power BI**. The goal is to move beyond a simple CSV-level analysis and simulate a more realistic analytics pipeline: data cleaning, data quality validation, relational redesign, SQL-based business analysis, dashboarding, and baseline predictive modeling.

The project was designed to reflect the kind of work expected in a **Data & Analytics internship**: handling raw data, checking data quality, restructuring data for analysis, generating business insights, and supporting decision-making with both descriptive and predictive analytics.

## Project Objectives
- Clean and validate raw telecom customer data.
- Build a small relational analytics environment from a flat dataset.
- Use SQL to answer churn-related business questions.
- Create dashboard-ready KPIs and segment insights.
- Support retention analysis with a baseline churn prediction model.

## Dataset
**Source:** Kaggle – Telco Customer Churn dataset  
**Original file used:** `WA_Fn-UseC_-Telco-Customer-Churn.csv`

Why this dataset was chosen:
- realistic enough for business analytics
- small enough to build quickly
- rich enough to support cleaning, SQL, dashboarding, and ML in one project

## Current Status
### Completed
- Raw CSV ingestion in pandas
- Data profiling (shape, columns, dtypes, missing values, duplicates)
- Cleaning and type correction for `TotalCharges`
- Data quality summary generation
- Split of the flat dataset into four logical tables
- Loading of those tables into SQLite
- Initial SQL business analysis

### In Progress / Optional Extensions
- Additional SQL segment analysis
- Power BI dashboard polish
- Baseline predictive modeling
- Final insight screenshots and report exports

## Folder Structure
```text
churn_project/
│
├── data/
│   ├── raw/
│   │   └── WA_Fn-UseC_-Telco-Customer-Churn.csv
│   ├── processed/
│   │   ├── churn_cleaned.csv
│   │   ├── churn_analytics.db
│   │   └── tables/
│   │       ├── customers.csv
│   │       ├── services.csv
│   │       ├── billing.csv
│   │       └── status.csv
│   └── quality/
│       ├── data_quality_report.csv
│       └── data_quality_summary.csv
│
├── notebooks/
│   ├── 01_data_cleaning_eda.ipynb
│   ├── 02_sql_analysis_notes.ipynb          # optional
│   └── 03_modeling.ipynb                    # optional
│
├── sql/
│   ├── schema.sql                           # optional for explicit SQL schema
│   ├── analysis_queries.sql
│   └── retention_queries.sql                # optional extension
│
├── dashboard/
│   ├── churn_dashboard.pbix                 # Power BI file
│   └── screenshots/                         # export visuals here
│
├── src/
│   ├── clean_data.py                        # optional script version of notebook logic
│   ├── split_tables.py                      # optional script version of notebook logic
│   ├── load_to_sqlite.py                    # optional script version of notebook logic
│   ├── data_quality_report.py               # optional script version
│   └── churn_model.py                       # optional model script
│
├── outputs/
│   ├── insights.txt
│   ├── metrics.txt
│   └── screenshots/
│
├── README.md
├── requirements.txt
└── .gitignore
```

## Four Logical Tables Created
The original dataset was a single flat table. It was reorganized into four logical tables to simulate a more realistic relational analytics design.

### 1. `customers`
Stores customer profile information.
- `customerID`
- `gender`
- `SeniorCitizen`
- `Partner`
- `Dependents`
- `tenure`

### 2. `services`
Stores service-subscription information.
- `customerID`
- `PhoneService`
- `MultipleLines`
- `InternetService`
- `OnlineSecurity`
- `OnlineBackup`
- `DeviceProtection`
- `TechSupport`
- `StreamingTV`
- `StreamingMovies`

### 3. `billing`
Stores contract and payment details.
- `customerID`
- `Contract`
- `PaperlessBilling`
- `PaymentMethod`
- `MonthlyCharges`
- `TotalCharges`

### 4. `status`
Stores the business outcome.
- `customerID`
- `Churn`

## Workflow
### Step 1 – Raw Data Ingestion
The CSV is loaded into pandas for quick inspection.

### Step 2 – Data Profiling
The dataset is checked for:
- shape
- columns
- dtypes
- missing values
- duplicates
- suspicious fields such as `TotalCharges`

### Step 3 – Cleaning and Type Correction
- `TotalCharges` is converted from text to numeric.
- Invalid values are coerced to `NaN`.
- Rows with invalid `TotalCharges` are removed.
- Text columns are stripped to remove hidden spacing issues.

### Step 4 – Data Quality Reporting
A structured report is created to summarize:
- data types
- missing values
- unique values
- rows removed
- duplicates after cleaning

### Step 5 – Relational Redesign
The flat table is split into `customers`, `services`, `billing`, and `status` to strengthen the SQL story and better reflect real-world business systems.

### Step 6 – SQLite Loading
The split tables are loaded into a local SQLite database for SQL querying.

### Step 7 – SQL Analytics
Core business analysis includes:
- overall churn rate
- churn by contract
- churn by payment method
- churn by internet service
- churn by tenure band
- revenue at risk

### Step 8 – Dashboard Layer
Power BI is used to create stakeholder-friendly KPI cards and segment visuals.

### Step 9 – Predictive Layer
A baseline logistic regression model can be added to estimate churn risk and support retention strategies.

## Key Results So Far
- Original dataset rows: **7043**
- Rows after cleaning: **7032**
- Invalid rows removed: **11**
- Duplicate rows after cleaning: **0**
- Overall churn rate: **26.58%**
- Month-to-month contract churn rate: **42.71%**
- One-year contract churn rate: **11.28%**
- Two-year contract churn rate: **2.85%**

These early results already show that contract type is a major driver of churn risk.

## Example SQL Queries
### Overall Churn Rate
```sql
SELECT
    COUNT(*) AS total_customers,
    SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) AS churned_customers,
    ROUND(100.0 * SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) / COUNT(*), 2) AS churn_rate_pct
FROM status;
```

### Churn by Contract
```sql
SELECT
    b.Contract,
    COUNT(*) AS total_customers,
    SUM(CASE WHEN s.Churn = 'Yes' THEN 1 ELSE 0 END) AS churned_customers,
    ROUND(
        100.0 * SUM(CASE WHEN s.Churn = 'Yes' THEN 1 ELSE 0 END) / COUNT(*),
        2
    ) AS churn_rate_pct
FROM billing b
JOIN status s
    ON b.customerID = s.customerID
GROUP BY b.Contract
ORDER BY churn_rate_pct DESC;
```

## How to Run the Project Locally
### 1. Create and activate a virtual environment
```powershell
python -m venv venv
.\\venv\\Scripts\\Activate.ps1
```

### 2. Install dependencies
```powershell
pip install pandas numpy matplotlib scikit-learn jupyter
```

### 3. Launch Jupyter
```powershell
jupyter notebook
```

### 4. Open the notebook
Open:
- `notebooks/01_data_cleaning_eda.ipynb`

### 5. Place the raw dataset here
- `data/raw/WA_Fn-UseC_-Telco-Customer-Churn.csv`

## Power BI Suggestions
Recommended report pages:

### Page 1 – Executive Overview
- Total Customers
- Churned Customers
- Churn Rate
- Revenue at Risk

### Page 2 – Churn Drivers
- Churn by Contract
- Churn by Payment Method
- Churn by Internet Service
- Churn by Tenure Band

### Page 3 – Retention Segments
- Senior vs Non-Senior churn
- Monthly charge patterns
- High-risk customer groups
- Retention recommendations

## Why This Project Matters
This project is relevant to real-world analytics because it demonstrates:
- data cleaning before analysis
- data quality awareness
- SQL-based segmentation and KPI calculation
- dashboard-oriented communication
- business framing around churn and revenue risk
- readiness to extend into ML-based decision support

## Interview Positioning
A strong way to describe this project:

> I built an end-to-end customer retention intelligence workflow using Python, SQLite, SQL, and Power BI. Starting from a raw telecom churn dataset, I cleaned and validated the data, reorganized it into a relational structure, generated churn and revenue-risk insights through SQL, and prepared a dashboard-driven analytics layer for business decision-making. I also designed the project to support a baseline predictive churn model.

## Possible Extensions
- random forest / XGBoost comparison
- cohort analysis by tenure band
- retention action simulation
- feature importance visualization
- automated pipeline scripts under `src/`

## Notes for GitHub Upload
Before uploading:
- make sure the folder structure matches this README
- include the cleaned outputs only if appropriate for your repo size
- add Power BI screenshots if the `.pbix` file is too large
- update the **Current Status** section honestly based on what is finished
- include only claims you can explain in an interview

## License
You can add an MIT License if you want this repository to be public and reusable.
