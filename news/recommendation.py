import pandas as pd
from sklearn.decomposition import TruncatedSVD
from sklearn.metrics.pairwise import cosine_similarity

# Load the data
df = pd.read_csv('news/preprocessed_bbc_news_data.csv')
df['category'] = df['category'].str.capitalize()

# Example user interaction data
interactions = {
    'user_id': [1, 1, 2, 2, 3, 3, 4, 4],
    'article_id': [1, 2, 2, 3, 3, 4, 4, 5],
    'interaction': [5, 4, 3, 5, 4, 2, 1, 4]
}
interactions_df = pd.DataFrame(interactions)

# Create user-item interaction matrix
user_item_matrix = interactions_df.pivot(index='user_id', columns='article_id', values='interaction').fillna(0)

# Apply matrix factorization using SVD
svd = TruncatedSVD(n_components=2)
latent_matrix = svd.fit_transform(user_item_matrix)

# Calculate cosine similarity
similarity_matrix = cosine_similarity(latent_matrix)

def get_recommendations(user_id, num_recommendations=2):
    similar_users = similarity_matrix[user_id - 1]
    similar_users_indices = similar_users.argsort()[::-1]
    
    recommendations = []
    for idx in similar_users_indices:
        if idx != user_id - 1:
            user_articles = user_item_matrix.iloc[idx].sort_values(ascending=False)
            for article_id, interaction in user_articles.items():  # Updated here
                if interaction > 0 and article_id not in recommendations:
                    recommendations.append(article_id)
                if len(recommendations) >= num_recommendations:
                    break
            if len(recommendations) >= num_recommendations:
                break
    return recommendations

# Get recommendations for a user
print(get_recommendations(1))
