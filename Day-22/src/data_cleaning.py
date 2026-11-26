import pandas as pd

# Data Cleaning Function
def clean_customer_data(df):

    # Make a Copy of Original Dataset
    df = df.copy()

    # 1. Remove Duplicate Records
    df = df.drop_duplicates()

    # 2. Handle Invalid Ages
    df.loc[(df["Age"] < 18) | (df["Age"] > 75), "Age"] = None

    # Fill Missing Ages with Median
    df["Age"] = df["Age"].fillna(df["Age"].median())

    # 3. Handle Missing Gender
    df["Gender"] = df["Gender"].fillna(df["Gender"].mode()[0])

    # 4. Correct Categorical Formatting
    df["Gender"] = df["Gender"].str.strip().str.title()
    df["City"] = df["City"].str.strip().str.title()

    # 5. Handle Invalid Monthly Charges
    df.loc[df["Monthly Charges"] < 0, "Monthly Charges"] = None

    df["Monthly Charges"] = df["Monthly Charges"].fillna(
        df["Monthly Charges"].median()
    )

    # 6. Handle Invalid Total Charges
    df.loc[df["Total Charges"] < 0, "Total Charges"] = None

    df["Total Charges"] = df["Total Charges"].fillna(
        df["Tenure"] * df["Monthly Charges"]
    )

    # Display Cleaning Results
    print("\nData Cleaning Completed!")
    print("Remaining Records:", len(df))
    print("Missing Values After Cleaning:", df.isnull().sum().sum())
    print("Duplicates After Cleaning:", df.duplicated().sum())

    return df