#One hot encoding

import pandas as pd
from sklearn.preprocessing import OneHotEncoder

data={
      'fruit':['Apple','Orange','Apple'],
      'Color':['Red','Orange','Green']
      }
df=pd.DataFrame(data)
print("Original DataSet:")
print(df)

one_hot_encoder=OneHotEncoder(sparse_output=False,drop='first')
one_hot_encoded=one_hot_encoder.fit_transform(df[['fruit','Color']])
features_names=one_hot_encoder.get_feature_names_out(['fruit','Color'])
df_one_hot=pd.DataFrame(one_hot_encoded,columns=features_names)

df_encoded=pd.concat([df.drop(['fruit','Color'],axis=1),df_one_hot],axis=1)
print("\n After One hot Encoding :")
print(df_encoded)