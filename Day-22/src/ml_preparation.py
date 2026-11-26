# Import Required Libraries
import pandas as pd
from pathlib import Path

# Machine Learning Dataset Preparation
def prepare_ml_dataset(df):

    # Make a Copy of Dataset
    df = df.copy()

    # Separate Features (X) and Target (y)
    X = df.drop(columns=["Customer ID", "Churn"])

    y = df["Churn"]

    # Convert Categorical Features into Numerical Values
    X = pd.get_dummies(
        X,
        columns=[
            "Gender",
            "City",
            "Contract Type",
            "Payment Method",
            "Internet Usage"
        ],
        dtype=int
    )

    # Convert Target into Numerical Values
    y = y.map({
        "No": 0,
        "Yes": 1
    })

    # Combine Features and Target
    ml_dataset = X.copy()
    ml_dataset["Churn"] = y

    # Save ML Ready Dataset
    project_path = Path(__file__).resolve().parents[1]

    output_path = (
        project_path
        / "data"
        / "processed"
        / "ml_ready_customer_data.csv"
    )

    ml_dataset.to_csv(output_path, index=False)

    print("\nML Dataset Preparation Completed!")
    print("Features Shape:", X.shape)
    print("Target Shape:", y.shape)
    print("ML Dataset Shape:", ml_dataset.shape)

    return X, y, ml_dataset