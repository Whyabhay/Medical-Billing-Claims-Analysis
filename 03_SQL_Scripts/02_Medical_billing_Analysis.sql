

# analysing how much each insurance provider is billed.
SELECT insurance_provider, SUM(billing_amount) AS total_billed 
FROM Patients 
GROUP BY insurance_provider;

# Count of patients by medical condition.
SELECT medical_condition, COUNT(*) AS total_patients 
FROM Patients 
GROUP BY medical_condition;

# Average billing amount by admission type.
SELECT admission_type, AVG(billing_amount) AS avg_bill_amount 
FROM Patients 
GROUP BY admission_type;

# List of emergency patients.alter
SELECT name, age, gender, hospital, billing_amount 
FROM Patients 
WHERE admission_type = 'Emergency';

# Patients with abnormal test results.
SELECT name, age, gender, medical_condition, test_results 
FROM Patients 
WHERE test_results = 'Abnormal';

# Total patients admitted per year
SELECT YEAR(date_of_admission) AS admission_year, COUNT(*) AS total_patients
FROM Patients
GROUP BY admission_year
ORDER BY admission_year DESC;

# Highest billing amount per hospital.
SELECT hospital, MAX(billing_amount) AS highest_bill 
FROM Patients 
GROUP BY hospital;

# Patients with highest bills.
SELECT name, age, hospital, billing_amount 
FROM Patients 
ORDER BY billing_amount DESC;

# Most commonly prescribed medications.
SELECT medication, COUNT(*) AS times_prescribed 
FROM Patients 
GROUP BY medication 
ORDER BY times_prescribed DESC;

# Patients who stayed more than 10 days.
SELECT name, date_of_admission, discharge_date,
DATEDIFF(discharge_date, date_of_admission) AS days_stayed 
FROM Patients 
WHERE DATEDIFF(discharge_date, date_of_admission) > 10;

# Total revenue Generated per year.
SELECT YEAR(date_of_admission) AS year, SUM(billing_amount) AS total_revenue 
FROM Patients 
GROUP BY year
ORDER BY year DESC;

# Monthly revenue analysis.
SELECT MONTH(date_of_admission) AS month, YEAR(date_of_admission) AS year, 
       SUM(billing_amount) AS monthly_revenue 
FROM Patients 
GROUP BY year, month
ORDER BY year DESC, month DESC;



