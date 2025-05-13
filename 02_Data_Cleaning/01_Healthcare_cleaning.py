import pandas as pd

# Loading the Excel file into a pandas DataFrame
df = pd.read_excel("healthcare.xlsx")

# Displaying the first 5 rows of the data to understand its structure
print(df.head())

# Showing the information about the DataFrame
print("\nColumn Info:")  
print(df.info())

# Checking for missing values in each column
print("\nMissing Values:")
print(df.isnull().sum())

# Checking for duplicate rows in the dataset
print("Duplicate rows:", df.duplicated().sum())

# Cleaning column names by converting to lowercase, and replacing spaces with underscores
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

# Converting the 'date_of_admission' and 'discharge_date' columns to datetime format
df['date_of_admission'] = pd.to_datetime(df['date_of_admission'], errors='coerce')
df['discharge_date'] = pd.to_datetime(df['discharge_date'], errors='coerce')

df['billing_amount'] = (
    df['billing_amount']
    .astype(str)
    .str.replace(r'[\$,]', '', regex=True)
    .astype(float))

# Dropping rows that have missing values in critical columns
df.dropna(subset=['name', 'age', 'gender', 'date_of_admission'], inplace=True)

# Filling other missing values
df['discharge_date'] = df['discharge_date'].fillna(pd.NaT)
df.fillna({'billing_amount': 0, 'room_number': 0}, inplace=True)

# Dropping duplicate rows
df.drop_duplicates(inplace=True)

# Type casting
df['age'] = df['age'].astype(int)
df['room_number'] = df['room_number'].astype(int)

# Saving the cleaned DataFrame to a new CSV file
print("\nCleaning done! File saved as 'healthcare_cleaned.csv'")
df.to_csv('healthcare_cleaned.csv', index=False)
