# Ethiopian Fintech Customer Analytics

## Project Overview

This project analyzes customer experiences with mobile banking applications from three major Ethiopian banks: Commercial Bank of Ethiopia (CBE), Bank of Abyssinia (BOA), and Dashen Bank. Through sentiment analysis and thematic classification of customer reviews, we identify key satisfaction drivers and pain points that influence customer perceptions.

## Repository Structure

```
fintech-customer-analytics/
│
├── data/                           # Data files
│   ├── scraped_reviews.csv         # Raw scraped reviews
│   ├── cleaned_reviews.csv         # Preprocessed reviews
│   ├── sentiment_theme_analysis.csv # Reviews with sentiment and theme labels
│   ├── theme_summary.csv           # Summary statistics by theme
│   └── bank_reviews.db             # SQLite database with all review data
│
├── scripts/                        # Python scripts
│   ├── scrape_reviews.py           # Script to scrape reviews from Google Play
│   ├── preprocess_data.py          # Data cleaning and preprocessing
│   ├── sentiment_analysis.py       # Sentiment analysis implementation
│   ├── db_operations.py            # Database operations (Oracle)
│   ├── create_sqlite_db.py         # SQLite database creation
│   ├── verify_db.py                # Database verification script
│   └── visualize_results.py        # Visualization generation
│
├── notebooks/                      # Jupyter notebooks
│   ├── Analytics.ipynb             # Main analysis notebook
│   ├── ThematicAnalysis.ipynb      # Thematic analysis notebook
│   ├── Insights_and_Recommendations.ipynb # Insights and recommendations
│   └── data/                       # Notebook-specific data
│
├── FINAL_REPORT.md                 # Final project report
└── README.md                       # This file
```

## Key Features

1. **Sentiment Analysis**: Dual-method approach using VADER and TextBlob to classify reviews as positive, neutral, or negative.
2. **Thematic Classification**: Categorization of reviews into seven key themes: Account Access, Transaction Performance, UI/UX, Reliability, Customer Support, Features, and Security.
3. **Comparative Analysis**: Cross-bank comparison to identify competitive advantages and gaps.
4. **Database Integration**: Relational database implementation for persistent storage and complex querying.
5. **Visualizations**: Data visualizations to highlight key findings and trends.

## Key Findings

- **Market Leader**: Dashen Bank leads with 72.7% positive sentiment and 4.4/5 average rating.
- **Critical Pain Points**: Reliability issues affect all banks but are most severe for BOA (50% negative).
- **Primary Satisfaction Drivers**: Security features, user interface, and transaction performance.

## Getting Started

### Prerequisites

- Python 3.8+
- Required packages: pandas, numpy, nltk, textblob, matplotlib, seaborn, sqlite3

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/fintech-customer-analytics.git

# Navigate to the project directory
cd fintech-customer-analytics

# Install required packages
pip install -r requirements.txt
```

### Usage

1. **Data Collection**:
   ```bash
   python scripts/scrape_reviews.py
   ```

2. **Data Preprocessing**:
   ```bash
   python scripts/preprocess_data.py
   ```

3. **Sentiment Analysis**:
   ```bash
   python scripts/sentiment_analysis.py
   ```

4. **Database Creation**:
   ```bash
   python scripts/create_sqlite_db.py
   ```

5. **Generate Visualizations**:
   ```bash
   python scripts/visualize_results.py
   ```

6. **Explore Notebooks**:
   - Open and run the Jupyter notebooks in the `notebooks/` directory for detailed analysis.

## Final Report

For a comprehensive analysis and recommendations, see the [Final Report](FINAL_REPORT.md).

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Google Play Store for providing access to customer reviews
- NLTK and TextBlob for sentiment analysis capabilities
- Ethiopian banking community for valuable insights
