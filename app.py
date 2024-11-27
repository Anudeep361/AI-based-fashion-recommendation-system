import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import openai
import numpy as np
import matplotlib.pyplot as plt

# Initialize OpenAI with the API key
openai.api_key = st.secrets["API_KEY"] 

@st.cache_data
def load_data(file_path):
    return pd.read_csv(file_path)

df = load_data('Fashion_products_catalog.csv')

def get_ratings_from_similarity(cosine_similarities, n_recommendations):
    # Normalize cosine similarities to a 0-10 rating scale
    ratings = cosine_similarities[:n_recommendations]
    ratings = (ratings / ratings.max()) * 10  # Normalize to a 0-10 scale
    return ratings.astype(int)  # Convert to integer values

def content_based_recommendation(query, df, n_recommendations=5):
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(df['Description'])
    query_vector = tfidf.transform([query])
    cosine_similarities = cosine_similarity(query_vector, tfidf_matrix).flatten()
    similar_indices = cosine_similarities.argsort()[-n_recommendations:][::-1]
    
    # Get ratings based on cosine similarities
    ratings_cb = get_ratings_from_similarity(cosine_similarities[similar_indices], n_recommendations)
    
    recommendations = df.iloc[similar_indices][['ProductName', 'Description', 'Price (INR)', 'ProductBrand']]
    return recommendations, ratings_cb

def gpt4_recommendation(query, df, n_recommendations):
    try:
        # Get a random sample of products from the catalog (for simplicity)
        sample_products = df[['ProductName', 'Description']].sample(n=n_recommendations)
        # Create a formatted input prompt for GPT-4
        product_list = "\n".join([f"{i+1}. {row['ProductName']} - {row['Description']}" for i, row in sample_products.iterrows()])
        prompt = f"Based on the following products, recommend {n_recommendations} products that best match the query '{query}':\n{product_list}. Keenly observe the number of items recommended. ensure you recommend {n_recommendations} items"

        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "system", "content": "You are a helpful assistant that recommends fashion products."},
                      {"role": "user", "content": prompt}],
            max_tokens=300,
            temperature=0.3
        )
        
        recommendations = response.choices[0].message['content'].strip()
        
        # Simulate ratings for GPT-4 recommendations (e.g., random ratings between 1 and 10)
        ratings_gpt4 = np.random.randint(1, 11, size=n_recommendations)
        
        return recommendations, ratings_gpt4
    except Exception as e:
        return f"An unexpected error occurred: {str(e)}", []

st.header("AN AI RECOMMENDER SYSTEM")
# Input query from user
query = st.text_input("Enter your fashion query (e.g., 'Outfit for a birthday party')")

# Number of recommendations to display
n_recommendations = st.slider("Number of Recommendations", min_value=1, max_value=10, value=5)

if st.button("Get Recommendations"):
    if query:
        # GPT-4 Recommendations with ratings
        st.subheader("GPT-4 Recommendations")
        gpt_recommendations, ratings_gpt4 = gpt4_recommendation(query, df, n_recommendations)  # Passing df along with query and n_recommendations
        st.write(gpt_recommendations)

        # Content-Based Recommendations with ratings
        st.subheader("Content-Based Recommendations")
        cb_recommendations, ratings_cb = content_based_recommendation(query, df, n_recommendations)
        st.write(cb_recommendations)

        # Rating Comparison
        st.subheader("Rating Comparison")
        plt.figure(figsize=(10, 6))
        plt.plot(ratings_gpt4, label="GPT-4 Ratings", linestyle="--", marker="o")
        plt.plot(ratings_cb, label="CBF Ratings", linestyle=":", marker="x")
        plt.xlabel("Product ID")
        plt.ylabel("Ratings")
        plt.title("Ratings Comparison")
        plt.legend()
        st.pyplot(plt)

    else:
        st.error("Please enter a query.")