# 🏥 Medical Billing and Insurance Claims Analysis

   This project focuses on analyzing a large healthcare dataset to extract actionable insights from medical billing and insurance claims. 
   It simulates a real-world analytics scenario using a combination of Python for data cleaning, SQL for structured analysis, and data visualization for 
   storytelling. The goal is to demonstrate end-to-end capabilities in handling messy healthcare data, deriving insights, and presenting findings effectively.

 ## Project Objective
    To clean and analyze healthcare billing and claims data in order to identify patterns in patient visits, billing amounts, medical conditions, and hospital 
    resource utilization.
    Additionally, this project aims to simulate the type of real-world business problem-solving expected in analytics roles. It focuses on identifying 
    inefficiencies in resource usage, financial trends in billing, and behavior patterns in patient claims. The objective is to not just analyze the data, but to 
    deliver clear, communicable findings that can support data-driven decision-making in the healthcare industry.

 ## Project Overview

 - **Dataset Size**: 55,000+ rows
 - **Data Source**: Publicly available Healthcare dataset from Kaggle
 - **Tools Used**: Python (Pandas,Matplotlib), MySQL, Excel
 - **Techniques Applied**:
  - Data Cleaning & Preprocessing.
  - SQL Querying & Analysis.
  - Data Visualization.
  - Debugging and Optimization.
 
 ## Scripts Overview

   # Healthcare_cleaning.py
   - Loads raw Excel data.
   - Strips and formats column names.
   - Converts date and numeric columns to proper data types.
   - Handles missing values.
   - Removes duplicates.
   - saves cleaned data to a CSV file.

   # Visualisations.py
   - Analyzes frequency of top medical conditions.
   - Visualizes billing amounts by gender.
   - Analyzes and plots patient age distributions.
   - Calculates and visualizes stay duration distributions.
   - Compares average billing across medical conditions
   - Displays monthly trend of patient visits
   - Shows average billing per patient per month
     
     All visualizations are created using matplotlib only, ensuring compatibility and simplicity

   # SQL Queries Overview
   - Imported cleaned data into MySQL using LOAD DATA INFILE.
   - Used SELECT, GROUP BY, and ORDER BY for aggregate analysis.
   - Filtered data using WHERE clause to isolate meaningful trends.
   - Joined data for enhanced relational insights (if applicable) .
   - Applied conditions to understand claim patterns, gender-based billing trends, top conditions, and admission counts.

 ## Process Summary
   - Data Cleaning: Cleaned raw data using Python and pandas — formatted dates, handled nulls, removed duplicates, and converted types.
   - SQL Import & Analysis: Imported cleaned CSV into MySQL for SQL-based exploration — filtering, aggregations, joins, and group analysis.
   - Visualization: Used Python (matplotlib) to generate insights with visuals — bar charts, histograms, etc.
   - 
 ## Challenges & Solutions
   - Date Parsing Errors: Solved by using errors='coerce' while converting to datetime.
   - Dirty Billing Data: Cleaned by removing currency symbols and converting to float.
   - Missing & Duplicate Data: Addressed using .dropna(), .fillna(), and .drop_duplicates().
   - Data Type Consistency: Explicit typecasting ensured uniformity.

 ## Conclusion
    This project demonstrates a clear pipeline from raw medical data to structured insights using SQL and Python. It highlights essential skills such as data 
    wrangling, SQL-based analytical reasoning, and effective visual communication with data. Together, these skills showcase an end-to-end understanding of data 
    workflows — making this project relevant for roles in healthcare analytics, finance, and broader data-driven industries. The structured process and documented 
    outputs also simulate a real-world business problem-solving scenario..

 
## 🙌 Let's Connect

   If you're a recruiter, fellow analyst, or enthusiast and would like to discuss this project, feel free to connect with me on
   [linkedin](https://www.linkedin.com/in/abhay-rana-76b724232/)
