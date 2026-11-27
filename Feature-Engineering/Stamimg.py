# Stemming 
import pandas as pd
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
import nltk

# Download necessary tokenizer data
nltk.download('punkt')

# Sample database
df = pd.DataFrame({
    'text': [
        'cats are running quickly',
        'dogs were barking loudly',
        'he studies in university',
        'they are enjoying the holiday',
        'ran fast'
    ]
})
print("Original DataFrame:")
print(df)
# Initialize stemmer
stemmer = PorterStemmer()
# Function to stem text
def stem_text(text):
    tokens = word_tokenize(text.lower())
    stem = [stemmer.stem(word) for word in tokens if word.isalpha()]
    return " ".join(stem)
# Apply stemming
df['stemmed_text'] = df['text'].apply(stem_text)
print("\nAfter stemming:")
print(df[['text', 'stemmed_text']])