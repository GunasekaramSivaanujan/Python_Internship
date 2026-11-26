import pandas as pd
import random
from pathlib import Path

# Generate Customer Dataset
def generate_customer_data():

    random.seed(42)

    # Customer Details
    genders = ["Male", "Female"]
    cities = ["Colombo", "Jaffna", "Kandy", "Galle", "Negombo"]

    contract_types = ["Monthly", "One Year", "Two Year"]

    payment_methods = [
        "Credit Card",
        "Bank Transfer",
        "Cash",
        "Online Payment"
    ]

    internet_usage = ["Low", "Medium", "High"]

    customer_records = []

    # Generate 5000 Customer Records
    for i in range(5000):

        customer_id = f"C{i + 1:05}"

        age = random.randint(18, 75)
        gender = random.choice(genders)
        city = random.choice(cities)

        tenure = random.randint(1, 72)

        monthly_charges = random.randint(1000, 10000)

        total_charges = tenure * monthly_charges

        contract_type = random.choice(contract_types)
        payment_method = random.choice(payment_methods)

        support_calls = random.randint(0, 15)

        usage = random.choice(internet_usage)

        # Generate Churn Status
        if support_calls > 8 or contract_type == "Monthly":
            churn = random.choices(
                ["Yes", "No"],
                weights=[60, 40]
            )[0]
        else:
            churn = random.choices(
                ["Yes", "No"],
                weights=[20, 80]
            )[0]

        customer_records.append([
            customer_id,
            age,
            gender,
            city,
            tenure,
            monthly_charges,
            total_charges,
            contract_type,
            payment_method,
            support_calls,
            usage,
            churn
        ])

    # Create DataFrame
    df = pd.DataFrame(customer_records, columns=[
        "Customer ID",
        "Age",
        "Gender",
        "City",
        "Tenure",
        "Monthly Charges",
        "Total Charges",
        "Contract Type",
        "Payment Method",
        "Support Calls",
        "Internet Usage",
        "Churn"
    ])

    # Add Sample Data Quality Issues

    # Missing Values
    df.loc[0:9, "Age"] = None
    df.loc[10:19, "Gender"] = None

    # Invalid Ages
    df.loc[20, "Age"] = -5
    df.loc[21, "Age"] = 150

    # Invalid Charges
    df.loc[22, "Monthly Charges"] = -1000
    df.loc[23, "Total Charges"] = -5000

    # Inconsistent Categorical Values
    df.loc[24, "Gender"] = "male"
    df.loc[25, "City"] = "COLOMBO"

    # Add Duplicate Records
    df = pd.concat([df, df.iloc[:50]], ignore_index=True)

    # Save Raw Dataset
    project_path = Path(__file__).resolve().parents[1]

    output_path = project_path / "data" / "raw" / "raw_customer_data.csv"

    df.to_csv(output_path, index=False)

    print("Customer Dataset Generated Successfully!")
    print("Total Records:", len(df))


# Run Dataset Generator
if __name__ == "__main__":
    generate_customer_data()