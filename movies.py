import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

df =  pd.read_csv("D:\Data Analyst Course\movie_dataset.csv", encoding="utf-8", delimiter=",", quoting=0, engine='python')

print(f"summary : \n{df.head()}")

print(f"Shape of dataset : \n{df.shape}")

print(f"columns are : \n{df.columns}")

##Cleaning
#remove unused columns
df = df.drop(columns=["overview", "tagline", "poster_path", "keywords", "homepage", "backdrop_path","imdb_id"])

#checking status
df = df.drop(df[df["status"]!="Released"].index)
df=df.drop(columns=["status"])



#cleaning NaN Valued Rows
df = df.dropna(subset=["title", "release_date","genres"])
df = df.dropna(subset=["production_companies", "production_countries", "spoken_languages"])


#Checking duplicates
#cleaning dupes
df = df.drop_duplicates()

#transform wrong type data
df['release_date'] = pd.to_datetime(df['release_date'])
df.info()
df['year'] = df['release_date'].dt.year
df = df.drop(df[df['year']<2000].index)
# count rows where year < 2000
count_before_2000 = df[df['year'] < 2000].shape[0]

print(f"Number of movies before 2000: {count_before_2000}")

###Analysis
##KPI
#Highest selling movies
top_selling_movie = df.sort_values(by='revenue', ascending=False).head(5)
print(f"top selling movies : \n{top_selling_movie[['title','revenue']]}")

#Best Return of Investment
df = df[df['budget']>0]
df = df[df['revenue']>0]
df['ROI'] = (df['revenue'] - df['budget'])/df['budget']
top_roi_movie = df.sort_values(by='ROI', ascending=False).head(5)
print(f"top Return of Investment movies are : \n{top_roi_movie[['title','ROI','budget']]}")

#best selling genres
df['genres'] = df['genres'].str.split(",")
df_exploded = df.explode('genres')
df_exploded['genres'] = df_exploded['genres'].str.strip().astype(str)
print(df_exploded['genres'].dtype)
df_genre = df_exploded.copy()

best_genres_sum = df_exploded.groupby('genres')['revenue'].sum().sort_values(ascending = False).head(5)


print(f"best selling genres : \n{best_genres_sum}")

#popularity of genres
popular_genres = df_exploded.groupby(['genres','year'])['popularity'].mean().sort_values(ascending = False)
print(f"Most popular Genres for movies : \n{popular_genres}")

#top studios by revenue
df['production_companies'] = df['production_companies'].str.split(',')
df_exploded = df.explode('production_companies')
df_exploded['production_companies'] = df_exploded['production_companies'].str.strip()

top_studios = df_exploded.groupby('production_companies')['revenue'].sum().sort_values(ascending = False).head(5)
print(f"top studios : \n {top_studios}")

##Visualization
#revenue by year 
revenue_by_year = df.groupby('year')['revenue'].sum().reset_index()
fig_rev_by_year = px.line(revenue_by_year, x='year', y='revenue', markers=True)
fig_rev_by_year.show()

#movie per year
movie_per_year = df.groupby('year')['id'].count()
fig_movie_per_year = px.line(movie_per_year, x=movie_per_year.index, y=movie_per_year.values, markers=True, labels = {"x" : "year", "y" :"Number Of Movies"})
fig_movie_per_year.show()

#revenue distribution by genre 
rev_per_genre= df_genre.groupby('genres')['revenue'].sum().sort_values(ascending = False).head(10)
fig_rev_per_genre= px.pie(values = rev_per_genre.values, names = rev_per_genre.index, title = "Top 10 Genres by Revenue")
fig_rev_per_genre.show() 

#top 10 ROI movies
top_ten_ROI_movies = df.sort_values(by = 'ROI', ascending=False).head(10)
fig_ROI = px.bar(top_ten_ROI_movies, x='title', y='ROI')
fig_ROI.show()

#Genre popularity overtime
popular_genres = popular_genres.reset_index()
fig_popularity_year = px.area(
    popular_genres,
    x = 'year',
    y = 'popularity',
    color= 'genres',
    title = 'Genre Popularity Over Time',
    labels = {'popularity' : 'Average Popularity', 'year' : 'Release Year'}
)
fig_popularity_year.show()


#df_cleaned = df.copy()
#df_companies = df_exploded.copy()


# Pick only the useful cleaned columns
#cleaned_cols = ['id', 'title', 'release_date', 'year', 'genres', 
                #'budget', 'revenue', 'popularity', 
                #'production_companies', 'production_countries', 'spoken_languages']

# Export the cleaned & exploded dataset
#df_companies[cleaned_cols].to_csv("D:/Data Analyst Course/movies_companies_cleaned.csv", 
                                 #index=False, encoding="utf-8")
#df_cleaned[cleaned_cols].to_csv("D:/Data Analyst Course/movies_cleaned.csv", 
                                 #index=False, encoding="utf-8")
#df_genre[cleaned_cols].to_csv("D:/Data Analyst Course/movies_genre_cleaned.csv", 
                                 #index=False, encoding="utf-8")

