# Fintech Customer Experience Analytics

## Overview

Analysis of customer reviews for Ethiopian banking apps to identify satisfaction drivers and pain points.

## Banks Analyzed

* Commercial Bank of Ethiopia (CBE)
* Bank of Abyssinia (BOA)
* Dashen Bank

## Methodology

1. **Data Collection**: Google Play Store API scraping
2. **Preprocessing**: Text cleaning, duplicate removal
3. **Quality Validation**: <5% missing data target

## Results

* Total Reviews: 1,031
* Data Quality: 97.3% complete
* Reviews per Bank: CBE (321), BOA (344), Dashen (366)

## Sentiment Insights

* **Dashen Bank**: 72.7% Positive | Avg Rating: 4.4 ★
* **CBE**: 61.1% Positive | Avg Rating: 4.1 ★
* **BOA**: 39.2% Positive | Avg Rating: 2.8 ★

## Usage

```bash
python scripts/scrape_reviews.py
python scripts/preprocess_data.py
```

## Next Steps

* Aspect-based sentiment analysis (Task 2)
* Theme and keyword extraction (Task 3)
* Database storage with Oracle (Task 4)
* Executive dashboard creation (Task 6)
