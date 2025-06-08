
import pandas as pd
import re
import logging
from datetime import datetime

logger = logging.getLogger(__name__)

class DataPreprocessor:
    def __init__(self, filepath):
        self.df = pd.read_csv(filepath)
        
    def clean_reviews(self):
        """Clean and preprocess review text"""
        logger.info("Cleaning review text...")
        
        # Remove duplicates
        initial_count = len(self.df)
        self.df = self.df.drop_duplicates(subset=['review', 'bank'])
        logger.info(f"Removed {initial_count - len(self.df)} duplicates")
        
        # Remove empty reviews
        self.df = self.df.dropna(subset=['review'])
        self.df = self.df[self.df['review'].str.strip() != '']
        
        # Clean text
        self.df['review_clean'] = self.df['review'].apply(self._clean_text)
        
        return self.df
    
    def _clean_text(self, text):
        """Clean individual review text"""
        if pd.isna(text):
            return ""
        
        # Convert to string and lowercase
        text = str(text).lower()
        
        # Remove extra whitespace
        text = re.sub(r'\s+', ' ', text)
        
        # Remove very short reviews (less than 10 characters)
        if len(text.strip()) < 10:
            return ""
            
        return text.strip()
    
    def validate_data(self):
        """Validate data quality"""
        total_reviews = len(self.df)
        missing_data = self.df.isnull().sum()
        
        logger.info(f"Total reviews: {total_reviews}")
        logger.info(f"Missing data:\n{missing_data}")
        
        # Check if we have enough reviews per bank
        bank_counts = self.df['bank'].value_counts()
        logger.info(f"Reviews per bank:\n{bank_counts}")
        
        # Calculate data quality score
        missing_percentage = (missing_data.sum() / (len(self.df) * len(self.df.columns))) * 100
        logger.info(f"Overall missing data: {missing_percentage:.2f}%")
        
        return missing_percentage < 5  # KPI: <5% missing data
    
    def save_cleaned_data(self, filename='data/cleaned_reviews.csv'):
        """Save cleaned data"""
        self.df.to_csv(filename, index=False)
        logger.info(f"Saved cleaned data to {filename}")

if __name__ == "__main__":
    preprocessor = DataPreprocessor('data/scraped_reviews.csv')
    preprocessor.clean_reviews()
    is_quality_good = preprocessor.validate_data()
    preprocessor.save_cleaned_data()
    
    print(f"Data quality check: {'PASSED' if is_quality_good else 'FAILED'}")