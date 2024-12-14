# -*- coding: utf-8 -*-
"""MRSAPRAC.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/14DUNP4H3Z7Gn3_dPkTiiew66t9YOx2sP
"""

import pandas as pd

# Install openpyxl if not already installed (needed for reading Excel files)
!pip install openpyxl --quiet

# Load the Excel file (replace 'path_to_your_file.xlsx' with the actual file path)
file_path = '/content/Table_1_MRSA_may_2024.xlsx'

# Load the entire Excel file
excel_data = pd.ExcelFile(file_path)

# Display the names of all sheets
print("Sheet Names:")
print(excel_data.sheet_names)

# Load each sheet into a dictionary for easier access
sheets_dict = {sheet_name: excel_data.parse(sheet_name) for sheet_name in excel_data.sheet_names}

# Display the first few rows of each sheet
for sheet_name, sheet_data in sheets_dict.items():
    print(f"\nSheet: {sheet_name}")
    print(sheet_data.head())

# Optionally, select a specific sheet for analysis
# Replace 'Sheet1' with the name of the sheet you want to analyze
specific_sheet_name = 'Sheet1'  # Change this to the desired sheet name
specific_data = sheets_dict[specific_sheet_name]

# Display information about the selected sheet
print("\nSelected Sheet Information:")
print(specific_data.info())

# Display summary statistics for the selected sheet
print("\nSummary Statistics for Selected Sheet:")
print(specific_data.describe())

import pandas as pd

# Specify the sheet to analyze
specific_sheet_name = 'data'  # Replace this if you want to analyze another sheet

# Load the selected sheet
specific_data = sheets_dict[specific_sheet_name]

# Clean and inspect the data
print("\nFirst few rows of the selected sheet:")
print(specific_data.head())

# Remove empty or NaN rows/columns (if applicable)
cleaned_data = specific_data.dropna(how='all')  # Drops rows/columns with all NaN values

# Display cleaned data
print("\nCleaned Data:")
print(cleaned_data.head())

# Display data information
print("\nData Information:")
print(cleaned_data.info())

# Summary statistics
print("\nSummary Statistics:")
print(cleaned_data.describe())

# Display current column names to identify the mismatch
print("Current Column Names:")
print(cleaned_data.columns)

# Rename columns (ensure the correct number matches the dataset)
cleaned_data.columns = [
    "Organisation_Type", "Organisation_Code", "Organisation_Name",
    "UKHSA_Centre", "ICB", "Region", "Year", "Month", "Metric",
    "Figure", "Data_Signed_Off", "Data_Changed_Since_Last_Publication", "Extra_Column"  # Add an extra column if needed
]

# Drop columns if necessary
columns_to_drop = ["Data_Signed_Off", "Data_Changed_Since_Last_Publication", "Extra_Column"]  # Adjust this as needed
cleaned_data = cleaned_data.drop(columns=columns_to_drop, errors='ignore')

# Display the first few rows of cleaned data
print("\nCleaned Data (First Few Rows):")
print(cleaned_data.head())

# Correct misaligned columns
cleaned_data["Region"] = cleaned_data["Year"]  # Move 'Region' data to its correct column
cleaned_data["Year"] = pd.to_numeric(cleaned_data["Month"], errors='coerce')  # Extract numerical 'Year'
cleaned_data["Month"] = pd.to_numeric(cleaned_data["Metric"], errors='coerce')  # Extract numerical 'Month'
cleaned_data["Figure"] = pd.to_numeric(cleaned_data["Figure"], errors='coerce')  # Convert 'Figure' to numeric

# Drop rows where 'Year' or 'Month' is NaN (invalid entries)
cleaned_data = cleaned_data.dropna(subset=["Year", "Month", "Figure"])

# Recheck column values
print("\nCleaned Data (First Few Rows After Corrections):")
print(cleaned_data.head())

# Check data types to confirm corrections
print("\nData Types:")
print(cleaned_data.dtypes)

# Save cleaned data for analysis
cleaned_data.to_csv("cleaned_mrsa_data.csv", index=False)
print("\nCleaned dataset saved as 'cleaned_mrsa_data.csv'.")

# Display the current column names to confirm the issue
print("Current Column Names:")
print(cleaned_data.columns)

# Update the renaming code to match the exact number of columns
cleaned_data.columns = [
    "Collection", "Organisation_Type", "Organisation_Code", "Organisation_Name",
    "UKHSA_Centre", "ICB", "Region", "Year", "Month", "Metric",
    "Figure", "Data_Signed_Off", "Data_Changed_Since_Last_Publication"
]

# Drop any irrelevant or unnecessary columns
columns_to_drop = ["Collection", "Data_Signed_Off", "Data_Changed_Since_Last_Publication"]
cleaned_data = cleaned_data.drop(columns=columns_to_drop, errors='ignore')

# Display the first few rows of the cleaned dataset
print("\nCleaned Data (First Few Rows):")
print(cleaned_data.head())

# Check for null values and data types
print("\nData Information:")
print(cleaned_data.info())

# Summarize MRSA cases by Year and Month
summary_by_time = cleaned_data.groupby(["Year", "Month"])["Figure"].sum().reset_index()
print("\nMRSA Cases by Year and Month:")
print(summary_by_time)

# Summarize MRSA cases by Metric
summary_by_metric = cleaned_data.groupby("Metric")["Figure"].sum().reset_index()
print("\nMRSA Cases by Metric:")
print(summary_by_metric)

# Plot trends over time (Year/Month)
import matplotlib.pyplot as plt
plt.figure(figsize=(10, 6))
for metric in cleaned_data["Metric"].unique():
    subset = cleaned_data[cleaned_data["Metric"] == metric]
    time_series = subset.groupby(["Year", "Month"])["Figure"].sum().reset_index()
    plt.plot(
        time_series["Month"] + (time_series["Year"] - cleaned_data["Year"].min()) * 12,
        time_series["Figure"],
        label=metric
    )
plt.xlabel("Time (Months)")
plt.ylabel("Number of Cases")
plt.title("MRSA Cases Over Time by Metric")
plt.legend()
plt.grid()
plt.show()

import pandas as pd

# Load the dataset (replace 'path_to_your_file.csv' with the correct file path in your Colab environment)
file_path = '/content/cleaned_mrsa_data.csv'

# Load the dataset into a Pandas DataFrame
mrsa_data = pd.read_csv(file_path)

# Display the first few rows to inspect the structure
print("First Few Rows of the Dataset:")
print(mrsa_data.head())

# Display basic information about the dataset
print("\nDataset Information:")
print(mrsa_data.info())

import os

# List files in the current directory to confirm the dataset upload
print("Files in the current directory:")
print(os.listdir('/content'))

# Check the content of the CSV file
with open('/content/cleaned_mrsa_data.csv', 'r') as file:
    content = file.read()

# Display the first few lines of the file
print("File Content (First 20 Lines):")
print('\n'.join(content.splitlines()[:20]))

# Reload the original Excel file to inspect its contents
excel_path = '/content/Table_1_MRSA_may_2024.xlsx'

# Load the Excel file and list sheet names
excel_data = pd.ExcelFile(excel_path)
print("Sheet Names in the Excel File:")
print(excel_data.sheet_names)

# Load and display the first few rows of the most likely data sheet (e.g., 'data')
sheet_name = 'data'  # Change this if necessary after checking sheet names
data = pd.read_excel(excel_path, sheet_name=sheet_name)

print("\nFirst Few Rows of the Data Sheet:")
print(data.head())

# Inspect current column names to resolve the mismatch
print("Current Column Names:")
print(data_cleaned.columns)

# Display the first few rows to check the structure
print("\nFirst Few Rows of the Dataset:")
print(data_cleaned.head())

# Rename columns to consistent and meaningful names
data_cleaned.columns = [
    "Collection", "Organisation_Type", "Organisation_Code", "Organisation_Name",
    "UKHSA_Centre", "ICB", "Region", "Year", "Month", "Metric",
    "Figure", "Data_Signed_Off", "Data_Changed_Since_Last_Publication"
]

# Drop unnecessary columns
data_cleaned = data_cleaned.drop(columns=["Collection", "Data_Signed_Off", "Data_Changed_Since_Last_Publication"], errors='ignore')

# Display the first few rows of the cleaned dataset
print("\nCleaned Data (First Few Rows):")
print(data_cleaned.head())

# Check the data types and missing values
print("\nData Information:")
print(data_cleaned.info())

# Aggregate MRSA cases by Metric
cases_by_metric = data_cleaned.groupby("Metric")["Figure"].sum().reset_index()
print("\nTotal MRSA Cases by Metric:")
print(cases_by_metric)

# Aggregate MRSA cases by Year and Month
cases_by_time = data_cleaned.groupby(["Year", "Month"])["Figure"].sum().reset_index()
print("\nTotal MRSA Cases by Year and Month:")
print(cases_by_time)

import matplotlib.pyplot as plt
import seaborn as sns

# Bar chart for MRSA cases by Metric
plt.figure(figsize=(10, 6))
sns.barplot(data=cases_by_metric, x="Metric", y="Figure", palette="viridis")
plt.title("Total MRSA Cases by Metric")
plt.xticks(rotation=45)
plt.xlabel("Metric")
plt.ylabel("Number of Cases")
plt.tight_layout()
plt.show()

# Line chart for MRSA cases over time
plt.figure(figsize=(12, 6))
plt.plot(cases_by_time["Month"] + (cases_by_time["Year"] - cases_by_time["Year"].min()) * 12,
         cases_by_time["Figure"], marker="o")
plt.title("MRSA Cases Over Time")
plt.xlabel("Time (Months)")
plt.ylabel("Number of Cases")
plt.grid()
plt.tight_layout()
plt.show()

# Aggregate MRSA cases by Region
cases_by_region = data_cleaned.groupby("Region")["Figure"].sum().reset_index()

# Sort regions by total cases for better visualization
cases_by_region = cases_by_region.sort_values("Figure", ascending=False)

# Bar chart for MRSA cases by Region
plt.figure(figsize=(12, 6))
sns.barplot(data=cases_by_region, x="Figure", y="Region", palette="coolwarm")
plt.title("Total MRSA Cases by Region")
plt.xlabel("Number of Cases")
plt.ylabel("Region")
plt.tight_layout()
plt.show()

# Display the aggregated data
print("\nTotal MRSA Cases by Region:")
print(cases_by_region)

import numpy as np

# Convert Year and Month to a single continuous variable (Months since start)
data_cleaned["Time"] = (data_cleaned["Year"] - data_cleaned["Year"].min()) * 12 + data_cleaned["Month"]

# Calculate correlation between Time and Figure
correlation = np.corrcoef(data_cleaned["Time"], data_cleaned["Figure"])[0, 1]
print(f"\nCorrelation between Time and MRSA Cases: {correlation:.2f}")

# Scatter plot for MRSA cases over time
plt.figure(figsize=(10, 6))
plt.scatter(data_cleaned["Time"], data_cleaned["Figure"], alpha=0.5)
plt.title("MRSA Cases Over Time")
plt.xlabel("Time (Months since start)")
plt.ylabel("Number of Cases")
plt.grid()
plt.tight_layout()
plt.show()

# Find the top 5 months with the highest MRSA cases
top_months = data_cleaned.groupby(["Year", "Month"])["Figure"].sum().sort_values(ascending=False).head(5).reset_index()
print("\nTop 5 Months with Highest MRSA Cases:")
print(top_months)

# Find the top 5 regions with the highest MRSA cases
top_regions = data_cleaned.groupby("Region")["Figure"].sum().sort_values(ascending=False).head(5).reset_index()
print("\nTop 5 Regions with Highest MRSA Cases:")
print(top_regions)