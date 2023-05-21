import pandas as pd
import numpy as np
import pickle

from datetime import datetime

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import classification_report, accuracy_score, precision_score, recall_score, f1_score
from sklearn.model_selection import train_test_split, GridSearchCV

#read files
df_vehicle = pd.read_csv('Data/Train Data/Train_Vehicle.csv')
df_claim = pd.read_csv('Data/Train Data/Train_Claim.csv')
df_demo = pd.read_csv('Data/Train Data/Train_Demographics.csv')
df_policy = pd.read_csv('Data/Train Data/Train_Policy.csv')
df_target = pd.read_csv('Data/Train Data/Traindata_with_Target.csv')

#we pivot the vehicles data
df_vehicle = df_vehicle.pivot(index="CustomerID", columns="VehicleAttribute", values="VehicleAttributeDetails").reset_index()

#drop any duplicate customers data
df_vehicle.drop_duplicates(subset='CustomerID', inplace=True)


#convert target columns to binary
df_target['ReportedFraud'].replace({'N':0, 'Y':1}, inplace=True)

#replace wrong entries
df_vehicle.replace({'???':np.NaN}, inplace=True)

#label encode the makes
make = {'Audi':1, 'Volkswagen':2, 'Toyota':3, 'Mercedes':4, 'Suburu':5, 'Saab':6,
       'Nissan':7, 'Ford':8, 'Accura':9, 'Dodge':10, 'Honda':11, 'Chevrolet':12, 'Jeep':13,
       'BMW':14}
df_vehicle['VehicleMake'].replace(make, inplace=True)

#drop cols
df_vehicle.drop(columns='VehicleModel', inplace=True)

#years from manufacture
df_vehicle['Years_from_man'] = datetime.now().year - pd.to_datetime(df_vehicle['VehicleYOM']).dt.year

#drop the years col
df_vehicle.drop(columns='VehicleYOM', inplace=True)

df_vehicle.drop(columns='VehicleID', inplace=True)


#convert to montyh wise numericals
df_claim['MonthOfIncident'] = pd.to_datetime(df_claim['DateOfIncident']).dt.month

#replace incorrect data
df_claim.replace({'?':np.NaN}, inplace=True)

#label the severity
severity = {'Trivial Damage':1, 'Minor Damage':2, 'Major Damage':3,'Total Loss':4 }
df_claim['SeverityOfIncident'].replace(severity, inplace=True)

#convert state label to just the numeric: state1 -> 1
df_claim['IncidentState'] = df_claim['IncidentState'].astype(str).apply(lambda x: x[-1] if len(x)==6 else None)
df_claim['IncidentCity'] = df_claim['IncidentCity'].astype(str).apply(lambda x: x[-1] if len(x)==5 else None)

df_claim.replace({'YES':1, 'NO':0}, inplace=True)
df_claim['Witnesses'].replace({'MISSINGVALUE':np.NaN}, inplace=True)
df_claim['Witnesses'] = df_claim['Witnesses'].astype('Int64')

ohe_cols = ['TypeOfIncident','TypeOfCollission','AuthoritiesContacted']
df_claim = pd.get_dummies(df_claim, prefix= ohe_cols, columns= ohe_cols, drop_first=True)

df_claim.drop(columns=['DateOfIncident','IncidentAddress'], inplace=True)

df_claim[['IncidentState','IncidentCity']] = df_claim[['IncidentState','IncidentCity']].astype('int64')

df_claim['AmountOfTotalClaim'].replace({'MISSEDDATA':np.NaN}, inplace=True)

df_claim['AmountOfTotalClaim'] = df_claim['AmountOfTotalClaim'].astype('float64')


#change the gender to binary
df_demo['InsuredGender'].replace({'MALE':1, "FEMALE":0}, inplace=True)
education = {'High School':1, 'College':2, 'Associate':3, 'Masters':4, 'MD':5, 'PhD':6, 'JD':7}
df_demo['InsuredEducationLevel'].replace(education, inplace=True)

ohe_cols_demo = ['InsuredOccupation','InsuredHobbies']
df_demo = pd.get_dummies(df_demo, prefix= ohe_cols_demo, columns= ohe_cols_demo, drop_first=True)
df_demo.drop(columns=['Country','InsuredZipCode'], inplace=True)

#convert to year
df_policy['DateOfPolicyCoverage'] = pd.to_datetime(df_policy['DateOfPolicyCoverage']).dt.year
df_policy['YearFromPolicyCoverage'] = datetime.now().year - df_policy['DateOfPolicyCoverage']

df_policy['InsurancePolicyState'] = df_policy['InsurancePolicyState'].astype(str).apply(lambda x: x[-1] if len(x)==6 else None)
df_policy['InsurancePolicyState'] = df_policy['InsurancePolicyState'].astype('int64')

df_policy[['Limit_1','Limit_2']] = df_policy['Policy_CombinedSingleLimit'].apply(lambda x: pd.Series(str(x).split("/")))

df_policy['Limit_1'] = df_policy['Limit_1'].astype('int64')
df_policy['Limit_2'] = df_policy['Limit_2'].astype('int64')

df_policy['Policy_CombinedSingleLimit'] = df_policy['Limit_1']/df_policy['Limit_2']

df_policy.drop(columns=['DateOfPolicyCoverage','Limit_1','Limit_2'], inplace=True)

df_policy.drop(columns='InsurancePolicyNumber', inplace=True)

ohe_cols_policy = ['InsuredRelationship']
df_policy = pd.get_dummies(df_policy, prefix= ohe_cols_policy, columns= ohe_cols_policy, drop_first=True)


#mergee
df_final = df_vehicle.merge(df_target, how='inner', on='CustomerID')
df_final = df_final.merge(df_claim, how='inner', on='CustomerID')
df_final = df_final.merge(df_demo, how='inner', on='CustomerID')
df_final = df_final.merge(df_policy, how='inner', on='CustomerID')

#null value drops
df_final.drop(columns=['PropertyDamage','PoliceReport'],inplace=True)
df_final.dropna(axis=0, inplace=True)

df_final.drop(columns='CustomerID', inplace=True)


#model building
#set X and y
X = df_final.drop(['ReportedFraud'], axis=1)
y = df_final['ReportedFraud']

#split into train test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

rf = RandomForestClassifier(random_state= 123, n_estimators=400, max_depth=15)
rf.fit(X_train, y_train)

y_pred=rf.predict(X_test)
score=accuracy_score(y_test,y_pred)

print('Score is',score)

pickle.dump(rf, open('model.pkl','wb'))