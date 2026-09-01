# Forward and Backward imputation for missing values in a dataset using Python
import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer

data ={
        'Name' :['Ram',np.nan,'Ankit','Rita','Golam'],
        'Age' :[35,np.nan,31,67,59],
        'Testscore':[85,90,np.nan,78,92],
        'Grade':['A','B',np.nan,'C','A']
}

df=pd.DataFrame(data)
print("Original Dataset:")
print(df)

df_f=df.ffill()
df_b=df.bfill()

print("\nDataset after Forward Imputation:")
print(df_f)

print("\nDataset after Backward Imputation:")
print(df_b)