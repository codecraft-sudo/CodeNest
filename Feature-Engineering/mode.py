# Mode imputation for missing values in a dataset using Python
import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer

data ={
        'Name' :['Ram','Sudev',np.nan,'Rita','Golam','Rita'],
        'Age' :[35,np.nan,31,67,59,67],
        'Testscore':[85,90,np.nan,78,92,90],
        'Grade':['A','B',np.nan,'C','A','B']
}

df=pd.DataFrame(data)
print("Original Dataset:")
print(df)

imputer=SimpleImputer(strategy='most_frequent')
df_imputed = pd.DataFrame(imputer.fit_transform(df[['Name', 'Age', 'Testscore', 'Grade']]), columns=['Name', 'Age', 'Testscore', 'Grade'])
df['Name'] = df_imputed['Name']
df['Age'] = df_imputed['Age']
df['Testscore'] = df_imputed['Testscore']
df['Grade'] = df_imputed['Grade']
print("\n After Imputation:")
print(df)