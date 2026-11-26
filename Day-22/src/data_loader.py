# Import Required Libraries
import pandas as pd
from pathlib import Path


# Load Customer Dataset
def load_customer_data():

    # Get Project Folder Path
    project_path = Path(__file__).resolve().parents[1]

    # CSV File Path
    file_path = project_path / "data" / "raw" / "raw_customer_data.csv"

    # Read CSV Dataset
    df = pd.read_csv(file_path)

    print("Customer Dataset Loaded Successfully!")

    return df