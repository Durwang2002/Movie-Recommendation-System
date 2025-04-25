import streamlit as st
import pandas as pd
import os

# ------------------ PAGE CONFIG ------------------
st.set_page_config(
    page_title="Movie Recommendation System",
    page_icon="🎬",
    layout="wide"
)

# ------------------ CUSTOM CSS FOR STYLING ------------------
st.markdown("""
    <style>
    body {
        background-color: #f9f9f9;
        color: #333333;
        font-family: 'Segoe UI', sans-serif;
    }

    .main-title {
        text-align: center;
        font-size: 3rem;
        font-weight: bold;
        color: #d32f2f;
        margin-top: 1rem;
        margin-bottom: 0.5rem;
        animation: fadeIn 2s ease;
    }

    .subtitle {
        text-align: center;
        color: #666666;
        font-size: 1.1rem;
        margin-bottom: 2rem;
        animation: fadeIn 2.5s ease;
    }

    input[type="text"] {
        border-radius: 10px;
        padding: 10px;
        font-size: 16px;
        border: 1px solid #ccc;
        width: 100%;
        margin-bottom: 1.5rem;
    }

    /* Fade animation */
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(-10px); }
        to { opacity: 1; transform: translateY(0); }
    }

    .dataframe th {
        background-color: #efefef;
    }

    .stDataFrameContainer {
        border-radius: 12px;
        overflow: hidden;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
    }

    .block-container {
        padding: 2rem;
    }

    </style>
""", unsafe_allow_html=True)

# ------------------ HEADER ------------------
st.markdown('<div class="main-title">🎬 Movie Recommendation System</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Find the best movies based on IMDb ratings</div>', unsafe_allow_html=True)

# ------------------ Load IMDb Data ------------------
BASE_DIR = r"C:\Users\durwa\Code Clause Internship Task\Movie_Recommendation_System"
BASICS_PATH = os.path.join(BASE_DIR, "MovieRecommender", "title.basics.tsv")
RATINGS_PATH = os.path.join(BASE_DIR, "MovieRecommender", "title.ratings.tsv")

@st.cache_data
def load_data():
    df_basics = pd.DataFrame()
    for chunk in pd.read_csv(BASICS_PATH, sep="\t", chunksize=10000, low_memory=False):
        filtered = chunk[chunk["titleType"] == "movie"][["tconst", "primaryTitle", "startYear", "genres"]]
        df_basics = pd.concat([df_basics, filtered])
    df_basics = df_basics.dropna(subset=["primaryTitle", "genres"]).reset_index(drop=True)

    df_ratings = pd.DataFrame()
    for chunk in pd.read_csv(RATINGS_PATH, sep="\t", chunksize=10000, low_memory=False):
        df_ratings = pd.concat([df_ratings, chunk[["tconst", "averageRating", "numVotes"]]])

    df_movies = pd.merge(df_basics, df_ratings, on="tconst")
    df_movies = df_movies[df_movies["numVotes"] >= 1000].reset_index(drop=True)
    return df_movies

df_movies = load_data()

# ------------------ SEARCH ------------------
search_query = st.text_input("🔍 Search for a movie title:")

# ------------------ RESULTS ------------------
if search_query:
    filtered_df = df_movies[df_movies['primaryTitle'].str.contains(search_query, case=False, na=False)]
    if not filtered_df.empty:
        st.markdown("### 🔍 Search Results")
        st.dataframe(
            filtered_df.sort_values(by="averageRating", ascending=False).reset_index(drop=True),
            use_container_width=True
        )
    else:
        st.warning("🚫 No matching movies found.")
else:
    st.markdown("### 🌟 Top Rated Movies (based on IMDb ratings):")
    top_movies = df_movies.sort_values(by="averageRating", ascending=False).head(10).reset_index(drop=True)
    st.dataframe(top_movies, use_container_width=True)

