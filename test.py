import pandas as pd

file_path = r"C:\Users\10817992\Downloads\testing_python.xlsx"

# Read first 9 rows, no header
data = pd.read_excel(file_path, sheet_name="Sheet1", header=None, engine="openpyxl")

# print(data.to_string(index=False))

csv_output_path = r"C:\Users\10817992\repos\excel_import\output.csv"
data.to_csv(csv_output_path, index=False)

print(f"CSV saved to {csv_output_path}")

#test