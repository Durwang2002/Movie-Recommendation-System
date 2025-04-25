## 🗃️ Dataset Details

**Note**: Due to the large size of the IMDb datasets, they are not included in this repository. To use the application, please download the required datasets manually from Kaggle:

1. Visit the [IMDb Datasets on Kaggle](https://www.kaggle.com/datasets/ashishjha/imdb-dataset) page.
2. Download the following files:
   - `title.basics.tsv`
   - `title.ratings.tsv`
3. Place the downloaded files in the following directory structure:



# 🎬 Movie Recommendation System

## 📌 Overview

The **Movie Recommendation System** is an intuitive web application designed to suggest movies based on user preferences. Leveraging IMDb datasets, the system filters movies by genre and rating, offering a seamless and personalized user experience.

## 🚀 Features

- **Interactive Filtering**: Select movies based on preferred genres and IMDb ratings.
- **Real-time Search**: Instantly search for movies by title.
- **Top-rated Suggestions**: View a curated list of top-rated movies.
- **Responsive Design**: Ensures optimal viewing across various devices.

## 🛠️ Technologies Used

- **Programming Language**: Python
- **Libraries & Frameworks**:
  - [Pandas](https://pandas.pydata.org/): Data manipulation and analysis.
  - [Streamlit](https://streamlit.io/): Web application development.
- **Version Control**: Git & GitHub
- **Data Source**: IMDb Datasets (`title.basics.tsv`, `title.ratings.tsv`)

## 🗃️ Dataset Details

The application utilizes IMDb's publicly available TSV files:

- **title.basics.tsv**: Contains information about movie titles, genres, and release years.
- **title.ratings.tsv**: Provides average ratings and the number of votes for each title.

These datasets are merged and preprocessed to ensure accurate and relevant movie recommendations.

## 🖥️ Installation & Usage

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Durwang2002/Movie-Recommendation-System

Install Dependencies: Ensure you have Python installed. Then, install the required libraries:
bash
pip install -r requirements.txt

Run the Application:

bash
streamlit run app.py
Access the Application: Open your browser and navigate to http://localhost:8501 to interact with the Movie Recommendation System.
