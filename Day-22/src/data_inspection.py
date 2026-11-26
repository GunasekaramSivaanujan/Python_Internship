# Dataset Inspection Function
def inspect_dataset(df):
    # 1. Dataset Shape
    print("\n========== DATASET SHAPE ==========")
    print("Rows and Columns:", df.shape)

    # 2. Column Names
    print("\n========== COLUMN NAMES ==========")
    print(df.columns.tolist())

    # 3. Data Types
    print("\n========== DATA TYPES ==========")
    print(df.dtypes)

    # 4. Missing Values
    print("\n========== MISSING VALUES ==========")
    print(df.isnull().sum())

    # 5. Duplicate Count
    print("\n========== DUPLICATE COUNT ==========")
    print(df.duplicated().sum())

    # 6. Statistical Summary
    print("\n========== STATISTICAL SUMMARY ==========")
    print(df.describe())

    # Return Inspection Information
    inspection_results = {
        "total_customers": len(df),
        "missing_values": int(df.isnull().sum().sum()),
        "duplicate_count": int(df.duplicated().sum())
    }

    return inspection_results