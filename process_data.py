import pandas as pd
import glob
import os

# Path to all CSV files in data folder
data_path = os.path.join("data", "*.csv")
files = glob.glob(data_path)

print(f"Found {len(files)} CSV files:", files)  # Debug check

# Read and combine all CSV files
all_data = pd.DataFrame()

for file in files:
    df = pd.read_csv(file)
    # Keep only rows where product is 'pink morsel'
    df = df[df["product"] == "pink morsel"]
    # Create a 'sales' column
    df["sales"] = df["quantity"] * df["price"]
    # Keep only the required columns
    df = df[["sales", "date", "region"]]
    all_data = pd.concat([all_data, df], ignore_index=True)

# Save to a new CSV
output_file = "formatted_sales.csv"
all_data.to_csv(output_file, index=False)

print(f"Formatted sales data saved to {output_file}")
