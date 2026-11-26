# Import Required Library
from pathlib import Path

# Generate Final Business Report
def generate_final_report(raw_df, clean_df, inspection_results):

    # 1. Total Customers
    total_customers = len(raw_df)

    # 2. Clean Customers
    clean_customers = len(clean_df)

    # 3. Removed Duplicates
    removed_duplicates = inspection_results["duplicate_count"]

    # 4. Missing Values Before Cleaning
    missing_before = inspection_results["missing_values"]

    # 5. Missing Values After Cleaning
    missing_after = int(clean_df.isnull().sum().sum())

    # 6. Churned Customers
    churned_customers = (clean_df["Churn"] == "Yes").sum()

    # 7. Churn Rate
    churn_rate = (churned_customers / clean_customers) * 100

    # 8. Average Monthly Charges
    average_monthly_charges = clean_df["Monthly Charges"].mean()

    # 9. Highest Churn Segment
    churn_by_contract = clean_df.groupby(
        "Contract Type"
    )["Churn"].apply(
        lambda x: (x == "Yes").mean() * 100
    )

    highest_churn_segment = churn_by_contract.idxmax()

    # Final Report Content
    report = f"""
========== CUSTOMER CHURN FINAL REPORT ==========

Total Customers: {total_customers}

Clean Customers: {clean_customers}

Removed Duplicates: {removed_duplicates}

Missing Values Before: {missing_before}

Missing Values After: {missing_after}

Churned Customers: {churned_customers}

Churn Rate: {churn_rate:.2f}%

Average Monthly Charges: {average_monthly_charges:.2f}

Highest Churn Segment: {highest_churn_segment}

=================================================
"""

    # Display Final Report
    print(report)

    # Save Final Report
    project_path = Path(__file__).resolve().parents[1]

    output_path = project_path / "reports" / "final_report.txt"

    with open(output_path, "w", encoding="utf-8") as file:
        file.write(report)

    print("Final Report Saved Successfully!")

    return report