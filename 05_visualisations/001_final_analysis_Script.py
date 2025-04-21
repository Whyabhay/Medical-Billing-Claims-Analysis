import pandas as pd
import matplotlib.pyplot as plt
#Loading Data
df = pd.read_csv("healthcare_cleaned_fixed.csv")

# Cleaning column names
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

# top 10 medical conditions
top_conditions = df['medical_condition'].value_counts().head(10)

# Bar chart
plt.figure(figsize=(10, 6))
top_conditions.plot(kind='bar', color='skyblue')
plt.title("Top 10 Medical Conditions")
plt.xlabel("Medical Condition")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


insurance_counts = df['insurance_provider'].value_counts().head(5)
# Pie chart
plt.figure(figsize=(8, 8))
plt.pie(insurance_counts.values, labels=insurance_counts.index, autopct='%1.1f%%', startangle=140)
plt.title("Patient Distribution by Insurance Provider")
plt.axis('equal') 
plt.tight_layout()
plt.show()

df['date_of_admission'] = pd.to_datetime(df['date_of_admission'], errors='coerce')
monthly_admissions = df.groupby(df['date_of_admission'].dt.to_period('M')).size().sort_index()
monthly_admissions.index = monthly_admissions.index.to_timestamp()

# Line Plot
plt.figure(figsize=(12, 6))
plt.plot(monthly_admissions.index, monthly_admissions.values, marker='o', linestyle='-', color='teal')
plt.title("Monthly Patient Admissions Over Time")
plt.xlabel("Month")
plt.ylabel("Number of Admissions")
plt.grid(True)
plt.tight_layout()
plt.show()



