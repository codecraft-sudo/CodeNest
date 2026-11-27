# Lammatisation 
import pandas as pd
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
import nltk

# Download required resources
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('wordnet')
nltk.download('omw-1.4')

# Sample dataset
df = pd.DataFrame({
    'text': [
        'cats are running quickly',
        'dogs were barking loudly',
        'he studies in university',
        'they are enjoying the holiday'
    ]
})
print("Original DataFrame:")
print(df)
# Initialize lemmatizer
lemmatizer = WordNetLemmatizer()

# Function to lemmatize text
def lemmatize_text(text):
    tokens = word_tokenize(text.lower())
    lemmas = [lemmatizer.lemmatize(word) for word in tokens if word.isalpha()]
    return " ".join(lemmas)

# Apply lemmatization
df['Lemmatized_text'] = df['text'].apply(lemmatize_text)

print("\nAfter Lemmatization:")
print(df[['text', 'Lemmatized_text']])