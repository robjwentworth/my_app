import cPickle as pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import pandas as pd

def build_model(filename):
    ### write your code to build a model
    # Define the vectorizer and model skeleton
    vectorizer = TfidfVectorizer(stop_words='english')
    model = MultinomialNB(alpha=0.1)
    # Fit the model
    df = pd.read_csv(filename)
    X = vectorizer.fit_transform(df['body'])
    y = df['section_name']
    model.fit(X,y)
    return vectorizer, model

if __name__ == '__main__':
    vectorizer, model = build_model('data/articles.csv')
    with open('data/vectorizer.pkl', 'w') as f:
        pickle.dump(vectorizer, f)
    with open('data/model.pkl', 'w') as f:
        pickle.dump(model, f)
