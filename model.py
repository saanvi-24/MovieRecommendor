import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_csv("movies.csv")

tfidf = TfidfVectorizer()
matrix = tfidf.fit_transform(df['genre'])

similarity = cosine_similarity(matrix)

def recommend(movie):
    movie = movie.lower()
    if movie not in df['title'].str.lower().values:
        return ["Movie not found"]

    idx = df[df['title'].str.lower() == movie].index[0]
    scores = list(enumerate(similarity[idx]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)[1:]

    return [df.iloc[i[0]].title for i in scores[:5]]