# 🎬 TMDB Movie Dataset Analysis

## 📌 Introduction
This project analyzes the **TMDB Movie Dataset** to uncover insights about revenue, profitability, genres, and studio performance.  
The dataset contains movie attributes such as title, release date, budget, revenue, genres, production companies, and languages.  

The main objectives are to:
- Understand revenue distribution and ROI
- Identify top-performing genres and studios
- Explore audience preferences and long-term industry patterns

---

## 🛠️ Data Cleaning
Steps taken to prepare the dataset:
- Dropped irrelevant columns (`overview`, `tagline`, `poster_path`, etc.)
- Removed unreleased movies
- Dropped rows with missing values in `title`, `release_date`, `genres`, `production_companies`, and `spoken_languages`
- Eliminated duplicates
- Converted `release_date` to datetime and extracted `year`

---

## 📊 Key Performance Indicators (KPIs)
1. **Top 5 Highest-Grossing Movies**  
2. **Best ROI (Return on Investment) Movies**  
3. **Top 5 Genres by Revenue**  
4. **Most Popular Genres (by average popularity score)**  
5. **Top 5 Studios by Revenue**  

---

## 📈 Insights
- **Highest Revenue Movies** → Blockbusters dominate, highlighting the strength of large-scale productions.  
- **Best ROI Movies** → Small, independent films often achieve exceptional ROI despite modest budgets.  
- **Genres** → Action, Adventure, and Sci-Fi lead in revenue; Comedy and Drama appear frequently but contribute less revenue.  
- **Genre Popularity** → Action and Adventure maintain steady audience demand across years.  
- **Studios** → Warner Bros. and Universal consistently dominate box office revenue.  

---

## 📉 Visualizations
Screenshots of Tableau dashboards (inserted here):

- **Revenue and Movies Released by Year**  
  ![Revenue by Year](visualizations/revenue_movies_by_year.png)

- **Top 10 Genres by Revenue (Pie Chart)**  
  ![Genres Revenue](visualizations/genres_revenue.png)

- **ROI Distribution (Bar Chart)**  
  ![ROI](visualizations/roi_distribution.png)

- **Genre Popularity Over Time (Stacked Area Chart)**  
  ![Genre Popularity](visualizations/genre_popularity.png)

---

## ✅ Conclusion
The TMDB dataset highlights clear industry patterns:
- Blockbusters drive the majority of revenue.
- Smaller productions can still achieve strong ROI.
- Action and Adventure genres dominate both in popularity and revenue.
- Established studios maintain long-term dominance.

These insights provide value for **investment strategy, audience targeting, and understanding long-term shifts in the film industry**.

---

## 📂 Repository Contents
- `movie_analysis.py` → Python cleaning & analysis script  
- `movies_clean.csv` → Cleaned dataset  
- `movies_exploded_genres.csv` → Exploded genre dataset  
- `movies_exploded_companies.csv` → Exploded production companies dataset  
- `visualizations/` → Tableau screenshots  
- `TMDB_Movie_Analysis_Polished.pdf` → Final report  

