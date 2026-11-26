# Import All Required Functions
from src.data_generator import generate_customer_data
from src.data_loader import load_customer_data
from src.data_inspection import inspect_dataset
from src.data_cleaning import clean_customer_data
from src.data_filtering import filter_customers
from src.data_analysis import analyze_customer_data
from src.ml_preparation import prepare_ml_dataset
from src.final_report import generate_final_report

# Main Project Execution
def main():

    print("\n===== CUSTOMER CHURN DATA PREPARATION SYSTEM =====")

    # Step 1: Generate Customer Dataset
    print("\n1. Generating Customer Dataset...")
    generate_customer_data()

    # Step 2: Load Dataset
    print("\n2. Loading Customer Dataset...")
    raw_df = load_customer_data()

    # Step 3: Inspect Dataset
    print("\n3. Inspecting Customer Dataset...")
    inspection_results = inspect_dataset(raw_df)

    # Step 4: Clean Dataset
    print("\n4. Cleaning Customer Dataset...")
    clean_df = clean_customer_data(raw_df)

    # Save Clean Dataset
    clean_df.to_csv(
        "Day-22/data/processed/clean_customer_data.csv",
        index=False
    )

    # Step 5: Filter Customers
    print("\n5. Filtering Customers...")
    filter_customers(clean_df)

    # Step 6: Analyze Customer Data
    print("\n6. Analyzing Customer Data...")
    analyze_customer_data(clean_df)

    # Step 7: Prepare ML Dataset
    print("\n7. Preparing ML Dataset...")
    prepare_ml_dataset(clean_df)

    # Step 8: Generate Final Report
    print("\n8. Generating Final Report...")
    generate_final_report(
        raw_df,
        clean_df,
        inspection_results
    )

    print("\n===== PROJECT COMPLETED SUCCESSFULLY! =====")


# Run Main Function
if __name__ == "__main__":
    main()