Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
= RESTART: C:\Users\Win-10\Desktop\Projects\Medical billing and insurance claims analysis\01_Healthcare_cleaning.py
            Name  Age  Gender  ... Discharge Date   Medication  Test Results
0  Bobby JacksOn   30    Male  ...     2024-02-02  Paracetamol        Normal
1   LesLie TErRy   62    Male  ...     2019-08-26    Ibuprofen  Inconclusive
2    DaNnY sMitH   76  Female  ...     2022-10-07      Aspirin        Normal
3   andrEw waTtS   28  Female  ...     2020-12-18    Ibuprofen      Abnormal
4  adrIENNE bEll   43  Female  ...     2022-10-09   Penicillin      Abnormal

[5 rows x 15 columns]

Column Info:
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 55500 entries, 0 to 55499
Data columns (total 15 columns):
 #   Column              Non-Null Count  Dtype         
---  ------              --------------  -----         
 0   Name                55500 non-null  object        
 1   Age                 55500 non-null  int64         
 2   Gender              55500 non-null  object        
 3   Blood Type          55500 non-null  object        
 4   Medical Condition   55500 non-null  object        
 5   Date of Admission   55500 non-null  datetime64[ns]
 6   Doctor              55500 non-null  object        
 7   Hospital            55500 non-null  object        
 8   Insurance Provider  55500 non-null  object        
 9   Billing Amount      55500 non-null  float64       
 10  Room Number         55500 non-null  int64         
 11  Admission Type      55500 non-null  object        
 12  Discharge Date      55500 non-null  datetime64[ns]
 13  Medication          55500 non-null  object        
 14  Test Results        55500 non-null  object        
dtypes: datetime64[ns](2), float64(1), int64(2), object(10)
memory usage: 6.4+ MB
None

Missing Values:
Name                  0
Age                   0
Gender                0
Blood Type            0
Medical Condition     0
Date of Admission     0
Doctor                0
Hospital              0
Insurance Provider    0
Billing Amount        0
Room Number           0
Admission Type        0
Discharge Date        0
Medication            0
Test Results          0
dtype: int64
Duplicate rows: 534

Cleaning done! File saved as 'healthcare_cleaned.csv'
