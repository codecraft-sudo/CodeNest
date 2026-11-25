import pandas as pd 
from sklearn.feature_extraction.text import CountVectorizer
#sample databaswe 
df=pd.DataFrame({
    'Text':[
        'cats are running quickly.',
        'Dogs were barking loudly.',
        'He studies in university.',
        'They are enjoying the holiday.'
    ]
})
print("Original Database")
print(df)
