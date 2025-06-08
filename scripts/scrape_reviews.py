from google_play_scraper import app, reviews, Sort
import pandas as pd
from datetime import datetime
import time
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class PlayStoreReviewScraper:
    def __init__(self):
        self.banks = {
            'CBE': 'com.combanketh.mobilebanking',
            'BOA': 'com.boa.boaMobileBanking', 
            'Dashen': 'com.dashen.dashensuperapp'
        }
        
    def scrape_bank_reviews(self, bank_name, app_id, count=400):
        """Scrape reviews for a specific bank app"""
        try:
            logger.info(f"Scraping reviews for {bank_name}...")
            
            # Get reviews
            result, continuation_token = reviews(
                app_id,
                lang='en',
                country='et',  # Ethiopia
                sort=Sort.NEWEST,
                count=count
            )
            
            # Process reviews
            processed_reviews = []
            for review in result:
                processed_reviews.append({
                    'review': review['content'],
                    'rating': review['score'],
                    'date': review['at'].strftime('%Y-%m-%d'),
                    'bank': bank_name,
                    'source': 'Google Play Store',
                    'reviewer': review['userName'],
                    'thumbs_up': review['thumbsUpCount']
                })
            
            logger.info(f"Scraped {len(processed_reviews)} reviews for {bank_name}")
            return processed_reviews
            
        except Exception as e:
            logger.error(f"Error scraping {bank_name}: {str(e)}")
            return []
    
    def scrape_all_banks(self):
        """Scrape reviews for all banks"""
        all_reviews = []
        
        for bank_name, app_id in self.banks.items():
            bank_reviews = self.scrape_bank_reviews(bank_name, app_id)
            all_reviews.extend(bank_reviews)
            
            # Be respectful - add delay between requests
            time.sleep(2)
        
        return all_reviews
    
    def save_to_csv(self, reviews, filename='data/scraped_reviews.csv'):
        """Save reviews to CSV"""
        df = pd.DataFrame(reviews)
        df.to_csv(filename, index=False)
        logger.info(f"Saved {len(reviews)} reviews to {filename}")
        return df

if __name__ == "__main__":
    scraper = PlayStoreReviewScraper()
    reviews = scraper.scrape_all_banks()
    df = scraper.save_to_csv(reviews)
    print(f"Total reviews collected: {len(reviews)}")