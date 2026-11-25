import pandas as pd 
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
import nltk
#Download required resourses
nltk.download('punkt')
nltk.download('Wordnet')
nltk.download('omw-1.4')
#sampple database
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
#initialise lemmatizer
lemmatizer=WordNetLemmatizer()
#Function to lemmatize text
def lemmatize_text(text):
    tokens=word_tokenize(text.lower())
    lemmas=[lemmatizer.lemmatize(word) for word in tokens if word.isalpha()]
    return" ".join(lemmas)
#Apply lkemmatization 
df['Lammatized_text']=df['Text'].apply(lemmatize_text)
print("\nAfter lammatization")
print(df[['Text','Lammatized_text']])    