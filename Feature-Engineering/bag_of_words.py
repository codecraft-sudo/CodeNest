# bag_of_words
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
#sample database 
df=pd.DataFrame({
    'text': [
            'cats are running quickly',
            'dogs were barking loudly',
            'he studies in university',
            'they are enjoying the holiday'
        ]
})
print("original database")
print(df)

#initilize count vectorize 
vectorize=CountVectorizer()
#fit and transform text data
x=vectorize.fit_transform(df['text'])
#convert to dfataframe
bow_df=pd.DataFrame(x.toarray(),columns=vectorize.get_feature_names_out())
print("\n bag of words rep")
print(bow_df)