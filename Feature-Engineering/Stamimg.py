
import pandas as pd
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
import nltk

# Download necessary tokenizer
nltk.download('punkt_tab')

# Sample database
df = pd.DataFrame({
    'Text': [
        'cats are running quickly.',
        'Dogs were barking loudly.',
        'He studies in university.',
        'They are enjoying the holiday.',
        'ran fast'
    ]
})

print("Original dataframe:")
print(df)

# Initialize stemmer
stemmer = PorterStemmer()

# Function to stem text
def stem_text(text):
    tokens = word_tokenize(text.lower())
    stem = [stemmer.stem(word) for word in tokens if word.isalpha()]
    return " ".join(stem)

# Apply stemming
df['stemmed_Text'] = df['Text'].apply(stem_text)

print("\nAfter stemming:")
print(df[['Text', 'stemmed_Text']])
#initializes count vectorize
vectorizer=Countvectorizer()
#fit and transform text data 
x=vectorizer.fit_transform(df['Text'])
#convert to dataFrame
bow_df=pd.DataFrame(x.toarray(),columns=vectorizer.get_feature_names_out())
print("\nbag of words representatijn")
print(bow_df)