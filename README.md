# ReviewInsight
ReviewInsight is a sentiment analysis platform for movie reviews, built using Python, Selenium, and Streamlit. It enables users to input IMDb review URLs, scrape public reviews, and analyze the sentiments (Positive, Negative, Neutral) using NLP-powered models. The app is intuitive and lightweight, with real-time results visualization and export capabilities.

## Features
- Scrape movie reviews from IMDb using Selenium.
- Analyze review sentiments using NLTK's Vader sentiment analyzer.
- Visualize results in a tabular format and sentiment bar chart.
- Download analyzed data as a CSV file.
- Fully interactive frontend powered by Streamlit.

## Usage:
### Basic setup and dependency management:
- Install `pipenv`:
```bash
pip install pipenv
```

- Activate the Virtual Environment:
```bash
pipenv shell
```

- Install required libraries from the `Pipfile.lock`:
```bash
pipenv install
```

OR

- Using pre-installed "venv" to create Virtual Environment:
```bash
python -m venv .venv
```

- Activate the Virtual Environment:
```bash
.venv/Scripts/activate.ps1
```

- Install all requirements from `requirements.txt`:
```bash
pip install -r requirements.txt
```

### Pre-requisites:
- ChromeDriver installed and added to PATH for Selenium to work.
- Internet connection for scraping and NLTK model download.

### To run the code:
- Launch the Streamlit application:
```bash
streamlit run app.py
```
- Access the application at `http://localhost:8501/` in your browser.

## Description about various files:
- **app.py**: Main application script. Contains function-based views for scraping reviews, analyzing sentiment, and rendering the UI.
- **Pipfile**: Defines all top-level project dependencies in a structured format.
- **Pipfile.lock**: Locks the exact versions of installed dependencies for consistent environments.
- **requirements.txt**: A flat list of dependencies exported from Pipenv for compatibility with pip-based deployments.