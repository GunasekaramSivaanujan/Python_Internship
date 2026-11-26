# Customer Filtering Functions
def filter_customers(df):

    # 1. High-Value Customers
    high_value_customers = df[
        df["Total Charges"] > df["Total Charges"].median()
    ]

    # 2. Customers with Many Support Calls
    many_support_calls = df[
        df["Support Calls"] > 8
    ]

    # 3. Customers with High Monthly Charges
    high_monthly_charges = df[
        df["Monthly Charges"] > df["Monthly Charges"].median()
    ]

    # 4. Customers Who Churned
    churned_customers = df[
        df["Churn"] == "Yes"
    ]

    # 5. Customers Who Stayed
    stayed_customers = df[
        df["Churn"] == "No"
    ]

    # Display Filtering Results
    print("\n========== CUSTOMER FILTERING ==========")

    print("High-Value Customers:", len(high_value_customers))
    print("Many Support Calls:", len(many_support_calls))
    print("High Monthly Charges:", len(high_monthly_charges))
    print("Churned Customers:", len(churned_customers))
    print("Customers Who Stayed:", len(stayed_customers))

    return {
        "high_value_customers": high_value_customers,
        "many_support_calls": many_support_calls,
        "high_monthly_charges": high_monthly_charges,
        "churned_customers": churned_customers,
        "stayed_customers": stayed_customers
    }