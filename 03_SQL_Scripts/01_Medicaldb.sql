CREATE DATABASE medicaldb;
USE medicaldb; 
CREATE TABLE Patients (
    name VARCHAR(100),
    age INT,
    gender VARCHAR(10),
    blood_type VARCHAR(50),
    medical_condition VARCHAR(50),
    date_of_admission DATE,
    doctor VARCHAR(100),
    hospital VARCHAR(100),
    insurance_provider VARCHAR(50),
    billing_amount DECIMAL(15,2),
    room_number INT,
    admission_type VARCHAR(50),
    discharge_date DATE,
    medication VARCHAR(100),
    test_results VARCHAR(50)
);

SET GLOBAL local_infile = 1;

LOAD DATA INFILE 'C://ProgramData//MySQL/MySQL Server 8.0//Uploads//healthcare_cleaned_fixed.csv'
INTO TABLE Patients
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"' 
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(name, age, gender, blood_type, medical_condition, date_of_admission, 
 doctor, hospital, insurance_provider, billing_amount, room_number, 
 admission_type, discharge_date, medication, test_results);
 
 SELECT * FROM patients;
 # Sample Data from kaggle Healthcare Dataset- EDA Cleaned and Imported Sucessfully