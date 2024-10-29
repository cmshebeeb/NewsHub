import pandas as pd

# Load the data
df = pd.read_csv('news/preprocessed_bbc_news_data.csv')
df['category'] = df['category'].str.capitalize()

# Display the first few rows of the dataframe
print(df.head())
