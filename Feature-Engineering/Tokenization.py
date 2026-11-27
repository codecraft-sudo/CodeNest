# Tokenisation 
import pandas as pd
from nltk.tokenize import word_tokenize
import nltk
#Download tokenize mpodels(only needed ones) 
nltk.download('punkt_tab')
#Sample dataset
df = pd.DataFrame({
    'Text': [
        'cats are running quickly.',
        'Dogs were barking loudly.',
        'He studies in university.',
        'They are enjoying the holiday.'
    ]
})
print("Original DataFrame")
print(df)
#Apply tokenization 
df['Tokens']=df['Text'].apply(lambda x:word_tokenize(x.lower()))
print("\n After Tokenization:")
print(df[['Text','Tokens']])