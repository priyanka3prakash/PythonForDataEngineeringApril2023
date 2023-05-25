import pandas as pd


df = pd.read_excel("/workspaces/PythonForDataEngineeringApril2023/11_File_operations/02_non_flat_files/e_xls/a_openpyxl/my_file.xlsx")

print(df.head())
print()

# Write the excel file 


data = {
    'Name': ['John', 'Emily', 'Michael', 'Sophia'],
    'Age': [25, 30, 35, 28],
    'City': ['New York', 'London', 'Paris', 'Tokyo'],
    'Salary': [5000, 6000, 7000, 5500]
}

df = pd.DataFrame(data)

# Write the DataFrame to an Excel file
df.to_excel('output.xlsx', index=False)
