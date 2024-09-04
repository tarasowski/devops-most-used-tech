import re
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import pandas as pd
import nltk
import os

nltk_data_dir = "/tmp/nltk_data"
nltk.data.path.append(nltk_data_dir)
os.environ['NLTK_DATA'] = nltk_data_dir

# Ensure NLTK data is downloaded to the correct directory
nltk.download('punkt', download_dir=nltk_data_dir)
nltk.download('stopwords', download_dir=nltk_data_dir)
nltk.download('wordnet', download_dir=nltk_data_dir)


def keyword_extractor(texts):
    # Preprocess the text data
    def preprocess(text):
        # Remove non-alphabetic characters
        text = re.sub(r'\W', ' ', text)
        # Convert to lowercase
        text = text.lower()
        # Tokenize the text
        words = word_tokenize(text)
        # Remove stop words
        stop_words = set(stopwords.words('english'))
        words = [word for word in words if word not in stop_words]
        # Lemmatize the words
        lemmatizer = WordNetLemmatizer()
        words = [lemmatizer.lemmatize(word) for word in words]
        return ' '.join(words)

    # Preprocess each text in the array
    processed_texts = [preprocess(text) for text in texts]

    # Extract keywords using TF-IDF
    # for bi-grams and tri-grams
    vectorizer = TfidfVectorizer(ngram_range=(1, 3))
    tfidf_matrix = vectorizer.fit_transform(processed_texts)
    feature_names = vectorizer.get_feature_names_out()

    # Convert TF-IDF matrix to a DataFrame
    df = pd.DataFrame(tfidf_matrix.toarray(), columns=feature_names)

    # Sum the occurrences of each n-gram across all documents
    keyword_counts = df.sum(axis=0).sort_values(ascending=False)

    # Optionally, convert to a dictionary for easier handling
    keyword_counts_dict = keyword_counts.to_dict()
    # change the sensivity of the TF IDF score, the lower the less relevant keywords will appear
    filtered_keyword_counts = {
        k: v for k, v in keyword_counts_dict.items() if 0.5 <= v <= 100}

    keyword_text_occurrences = {
        keyword: 0 for keyword in filtered_keyword_counts}

    for keyword in filtered_keyword_counts:
        for text in processed_texts:
            if keyword in text:
                keyword_text_occurrences[keyword] += 1

    sorted_keyword_text_occurrences = dict(sorted(
        keyword_text_occurrences.items(), key=lambda item: item[1], reverse=True))

    return sorted_keyword_text_occurrences
