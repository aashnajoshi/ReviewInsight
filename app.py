import streamlit as st
from selenium import webdriver
from selenium.webdriver.common.by import By
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk
import pandas as pd
import time

nltk.download('vader_lexicon')

# ---------- Web Scraping ----------
def scrape_reviews(movie_url, max_reviews=30):
    st.info("Launching browser...")
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    reviews = []
    try:
        driver.get(movie_url)
        time.sleep(3)
        while len(reviews) < max_reviews:
            review_elements = driver.find_elements(By.CLASS_NAME, "text.show-more__control")
            for elem in review_elements:
                text = elem.text.strip()
                if text and text not in reviews: reviews.append(text)
                if len(reviews) >= max_reviews: break
            try:
                load_more = driver.find_element(By.ID, "load-more-trigger")
                driver.execute_script("arguments[0].click();", load_more)
                time.sleep(2)
            except: break
    finally: driver.quit()
    return reviews

# ---------- Sentiment Analysis ----------
def analyze_sentiments(reviews):
    sia = SentimentIntensityAnalyzer()
    analyzed_data = []
    for review in reviews:
        score = sia.polarity_scores(review)
        sentiment = "Positive" if score['compound'] > 0.05 else "Negative" if score['compound'] < -0.05 else "Neutral"
        analyzed_data.append({"review": review, "sentiment": sentiment, "score": score['compound']})
    return pd.DataFrame(analyzed_data)

# ---------- UI Layout ----------
def main():
    st.set_page_config(page_title="🎬 ReviewInsight", layout="centered")
    st.title("🎬 ReviewInsight")
    st.markdown("Enter an IMDb movie reviews page URL to analyze public sentiment.")
    movie_url = st.text_input("IMDb Reviews URL", value="https://www.imdb.com/title/tt0111161/reviews")
    max_reviews = st.slider("Number of Reviews to Analyze", 10, 100, 30)
    if st.button("Analyze"):
        with st.spinner("Scraping reviews and analyzing sentiment..."):
            reviews = scrape_reviews(movie_url, max_reviews)
            if not reviews:
                st.error("No reviews found or unable to scrape the site.")
                return
            df = analyze_sentiments(reviews)
            st.success(f"Analyzed {len(df)} reviews.")
            st.dataframe(df[['review', 'sentiment', 'score']])
            st.bar_chart(df['sentiment'].value_counts())
            st.download_button("Download Results as CSV", df.to_csv(index=False), file_name="movie_sentiments.csv")

if __name__ == "__main__":
    main()