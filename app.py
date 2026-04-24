import streamlit as st
import requests
from model import recommend

# 🔑 Replace with your TMDB API key
API_KEY = ""


# 🎬 Function to fetch poster
def fetch_poster(movie_name):
    try:
        url = "https://api.themoviedb.org/3/search/movie"
        
        params = {
            "api_key": API_KEY,
            "query": movie_name
        }

        response = requests.get(url, params=params, timeout=10)
        data = response.json()

        if data and data.get("results"):
            for movie in data["results"]:
                if movie.get("poster_path"):
                    return "https://image.tmdb.org/t/p/w500" + movie["poster_path"]

    except Exception as e:
        print("Error:", e)

    return "https://via.placeholder.com/150?text=No+Image"


# 🌐 Streamlit UI
st.set_page_config(page_title="Movie Recommender", page_icon="🎬")

st.title("🎬 Movie Recommendation System")

st.write("Get movie suggestions with posters using AI 🎯")


# 🎯 Input
movie = st.text_input("Enter a movie name (e.g., Inception, Titanic):")


# 🚀 Button
if st.button("Recommend"):
    if movie:
        results = recommend(movie)

        st.write("### 🎥 Recommended Movies:")

        cols = st.columns(3)

        for i, r in enumerate(results):
            with cols[i % 3]:
                poster = fetch_poster(r)

                if poster:
                    st.image(poster)
                else:
                    st.image("https://via.placeholder.com/150?text=No+Image")

                st.write(f"**{r}**")

    else:
        st.warning("Please enter a movie name")


# 👇 Footer (looks professional)
st.markdown("---")
st.markdown("Made with ❤️ using Python, Streamlit & TMDB API")
