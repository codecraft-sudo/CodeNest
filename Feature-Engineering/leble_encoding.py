import pandas as pd
from sklearn.preprocessing import LabelEncoder

data={
    'fruit':['Apple','Banana','Orange','Apple','Banana'],
    'color':['Red','Yellow','Orange','Green','Yellow']
}

df=pd.DataFrame(data)
print("Original dataset ::")
print(df)

lebel_encoder=LabelEncoder()
df_lebel_encoded=df.copy()
df_lebel_encoded['fruit']=lebel_encoder.fit_transform(df['fruit'])
df_lebel_encoded['color']=lebel_encoder.fit_transform(df['color'])

print("\n After lebel Encoding ::")
print(df_lebel_encoded)