import pandas as pd
import numpy as np
from joblib import load  # saving the model
from ConvertColumns import SingleColumn

RFC = load("RandomForestClassifier - HeartDisease.h5")
SC = load("StandardScaler - HeartDisease.h5")

columns = ['BMI', 'Smoking', 'AlcoholDrinking', 'Stroke', 'PhysicalHealth',
       'MentalHealth', 'DiffWalking', 'Sex', 'AgeCategory', 'Diabetic',
       'PhysicalActivity', 'SleepTime', 'Asthma', 'KidneyDisease',
       'SkinCancer', 'Asian', 'Black', 'Hispanic', 'Other', 'White', 'Fair',
       'Good', 'Poor', 'Very good']

inserted_data = []

for col_name in columns:
    if col_name == "AgeCategory":
        print("{:_^50}".format("Age range: 18-24, 25-29, 30-34, 35-39, 40-44, 45-49, 50-54, 55-59, 60-64, 65-69, 70-74, 75-79, 80 "))
    elif col_name in ["Smoking", "AlcoholDrinking", "Stroke", "DiffWalking", "Diabetic", "Asthma", "KidneyDisease", "SkinCancer","PhysicalActivity"]:
        print("{:_^50}".format("Yes or No"))
    elif col_name in ["BMI", "PhysicalHealth", "MentalHealth", "SleepTime"]:
        print("{:_^50}".format("Chose range from 0-30"))
    elif col_name == "Sex":
        print("{:_^50}".format("Male or Female"))
    else:
        print("{:_^70}".format("Choose only one Type 1 means Yes and define all 0`s"))
    inserted = input(f"Describe your health on pos {len(inserted_data)}: {col_name} \t")
    
    inserted_data.append(inserted)

test_data = pd.DataFrame(pd.Series(np.array(inserted_data))).T
test_data.columns = columns

for col_name in ["Smoking","AlcoholDrinking","Stroke","DiffWalking", "SkinCancer", "Diabetic", "PhysicalActivity", "Asthma","KidneyDisease"]:
    test_data[col_name] = test_data[col_name].apply(lambda x: 1 if x == "Yes" else 0)

test_data['AgeCategory'] = test_data['AgeCategory'].apply(SingleColumn.AgeCategory)
test_data["Sex"] = test_data["Sex"].apply(lambda x: 1 if x == "Male" else 0)

# predict Heart Health
scaled = SC.transform(test_data)

patient_descriptions = pd.DataFrame(scaled, columns =  columns)

PredictHealth = RFC.predict(patient_descriptions)

if PredictHealth[0] == 0:
    print("\n You are Healthy you didn`t have HeartDisease")
    
elif PredictHealth[0] == 1:
    print("\n Sorry you have had HeartDisease you should talk to your doctor immediately")
    