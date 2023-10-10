import os
import pandas as pd

# Directory containing the CSV files
folder_path = "precipitation_csv"

# List all CSV files in the folder
csv_files = [file for file in os.listdir(folder_path) if file.endswith(".csv")]

# Initialize an empty DataFrame to store the merged data
merged_data = pd.DataFrame()

# Loop through the CSV files and merge them
for csv_file in csv_files:
    # Construct the full file path
    file_path = os.path.join(folder_path, csv_file)
    
    # Read each CSV file into a DataFrame
    df = pd.read_csv(file_path)
    
    # Append the data to the merged_data DataFrame
    merged_data = merged_data.append(df, ignore_index=True)

# Save the merged data to a new CSV file
merged_data.to_csv("merged_data.csv", index=False)

print("CSV files inside 'precipitation_csv' folder have been merged and saved as merged_data.csv")
