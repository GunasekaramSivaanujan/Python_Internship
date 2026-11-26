# Import Required Libraries
import pandas as pd
from pathlib import Path

# Customer Data Analysis Function
def analyze_customer_data(df):

    # Create Reports Folder Path
    project_path = Path(__file__).resolve().parents[1]
    reports_path = project_path / "reports"

    # Create Customer Type Based on Tenure
    df = df.copy()

    df["Customer Type"] = pd.cut(
        df["Tenure"],
        bins=[0, 12, 36, 72],
        labels=["New", "Regular", "Loyal"]
    )

    # 1. Churn by Contract Type
    churn_by_contract = pd.crosstab(
        df["Contract Type"],
        df["Churn"]
    )

    # 2. Churn by City
    churn_by_city = pd.crosstab(
        df["City"],
        df["Churn"]
    )

    # 3. Average Charges by Customer Type
    average_charges = df.groupby(
        "Customer Type",
        observed=False
    )["Monthly Charges"].mean()

    # 4. Average Support Calls by Churn Status
    average_support_calls = df.groupby(
        "Churn"
    )["Support Calls"].mean()

    # Display Analysis Results
    print("\n========== CUSTOMER ANALYSIS ==========")

    print("\nChurn by Contract Type:")
    print(churn_by_contract)

    print("\nChurn by City:")
    print(churn_by_city)

    print("\nAverage Charges by Customer Type:")
    print(average_charges)

    print("\nAverage Support Calls by Churn Status:")
    print(average_support_calls)

    # Export Analysis Reports
    churn_by_contract.to_csv(
        reports_path / "churn_by_contract.csv"
    )

    churn_by_city.to_csv(
        reports_path / "churn_by_city.csv"
    )

    average_charges.to_csv(
        reports_path / "average_charges_by_customer_type.csv"
    )

    average_support_calls.to_csv(
        reports_path / "average_support_calls_by_churn.csv"
    )

    print("\nCustomer Analysis Reports Exported Successfully!")

    return {
        "churn_by_contract": churn_by_contract,
        "churn_by_city": churn_by_city,
        "average_charges": average_charges,
        "average_support_calls": average_support_calls
    }