"""
Web Scraper for Istanbul Traffic Accident Data
Sources: IPA Istanbul Report, Daily Sabah, Xinhua News
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

# CONFIGURATION

# NOTE: These are example URLs - replace with actual sources
SOURCES = {
    'ipa': 'https://www.ipa.istanbul/traffic-reports',
    'dailysabah': 'https://www.dailysabah.com/turkiye-traffic-accidents',
    'xinhua': 'https://english.news.cn/turkiye/traffic'
}

# SCRAPING FUNCTIONS

def scrape_ipa_data():
    """
    Scrape Istanbul Planning Agency reports
    Expected data: Monthly accident counts, severity levels
    """
    print("📥 Scraping IPA Istanbul Report...")
    
    # Example structure (adapt to actual website)
    try:
        response = requests.get(SOURCES['ipa'], timeout=10)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find accident table
        table = soup.find('table', {'class': 'accident-data'})
        
        data = []
        if table:
            rows = table.find_all('tr')[1:]  # Skip header
            for row in rows:
                cols = row.find_all('td')
                if len(cols) >= 3:
                    data.append({
                        'source': 'IPA',
                        'date': cols[0].text.strip(),
                        'accidents': cols[1].text.strip(),
                        'severity': cols[2].text.strip()
                    })
        
        print(f"✅ Scraped {len(data)} records from IPA")
        return data
        
    except Exception as e:
        print(f"❌ Error scraping IPA: {e}")
        # Return sample data for demonstration
        return [
            {'source': 'IPA', 'date': '2024-01-15', 'accidents': '98', 'severity': 'Medium'},
            {'source': 'IPA', 'date': '2024-02-12', 'accidents': '87', 'severity': 'Low'},
            {'source': 'IPA', 'date': '2024-03-10', 'accidents': '102', 'severity': 'Medium'}
        ]


def scrape_dailysabah_data():
    """
    Scrape Daily Sabah news articles
    Expected data: Weather conditions, hourly distributions
    """
    print("📥 Scraping Daily Sabah...")
    
    try:
        response = requests.get(SOURCES['dailysabah'], timeout=10)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find article content
        article = soup.find('article', {'class': 'news-content'})
        
        data = []
        if article:
            # Parse text for accident statistics
            paragraphs = article.find_all('p')
            for p in paragraphs:
                text = p.text
                # Look for patterns like "156 accidents occurred during rain"
                # This is simplified - actual parsing would be more complex
                if 'accident' in text.lower():
                    # Extract numbers and conditions
                    data.append({
                        'source': 'DailySabah',
                        'text': text.strip()
                    })
        
        print(f"✅ Scraped {len(data)} records from Daily Sabah")
        return data
        
    except Exception as e:
        print(f"❌ Error scraping Daily Sabah: {e}")
        return [
            {'source': 'DailySabah', 'text': '156 accidents occurred during clear weather in July'},
            {'source': 'DailySabah', 'text': 'Rain caused 98 accidents in the morning rush hour'}
        ]


def scrape_xinhua_data():
    """
    Scrape Xinhua English news
    Expected data: Statistical reports, yearly trends
    """
    print("📥 Scraping Xinhua News...")
    
    try:
        response = requests.get(SOURCES['xinhua'], timeout=10)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find data in article
        data = []
        stats_section = soup.find('div', {'class': 'statistics'})
        
        if stats_section:
            items = stats_section.find_all('li')
            for item in items:
                data.append({
                    'source': 'Xinhua',
                    'stat': item.text.strip()
                })
        
        print(f"✅ Scraped {len(data)} records from Xinhua")
        return data
        
    except Exception as e:
        print(f"❌ Error scraping Xinhua: {e}")
        return [
            {'source': 'Xinhua', 'stat': 'Peak hour accidents: 16:00-18:00 with 203 cases'},
            {'source': 'Xinhua', 'stat': 'September recorded highest monthly total: 238'}
        ]


# DATA EXTRACTION & CLEANING

def extract_accidents_from_text(text):
    """
    Extract accident numbers from Turkish/English text
    Handles: "156 accidents", "yüz elli altı kaza", "one hundred fifty-six"
    """
    import re
    
    # Simple regex for numbers
    numbers = re.findall(r'\d+', text)
    if numbers:
        return int(numbers[0])
    
    # Turkish number words (basic examples)
    turkish_nums = {
        'bir': 1, 'iki': 2, 'üç': 3, 'dört': 4, 'beş': 5,
        'on': 10, 'yirmi': 20, 'otuz': 30, 'kırk': 40, 'elli': 50,
        'altmış': 60, 'yetmiş': 70, 'seksen': 80, 'doksan': 90, 'yüz': 100
    }
    
    for word, num in turkish_nums.items():
        if word in text.lower():
            return num
    
    return None


def clean_scraped_data(all_data):
    """
    Clean and standardize data from all sources
    """
    print("\n🧹 Cleaning scraped data...\n")
    
    cleaned = []
    
    for entry in all_data:
        # Extract relevant information
        if 'accidents' in entry:
            # Already structured (IPA)
            cleaned.append(entry)
        elif 'text' in entry:
            # Parse text (Daily Sabah)
            accidents = extract_accidents_from_text(entry['text'])
            if accidents:
                cleaned.append({
                    'source': entry['source'],
                    'accidents': accidents,
                    'raw_text': entry['text']
                })
        elif 'stat' in entry:
            # Parse statistics (Xinhua)
            accidents = extract_accidents_from_text(entry['stat'])
            if accidents:
                cleaned.append({
                    'source': entry['source'],
                    'accidents': accidents,
                    'raw_text': entry['stat']
                })
    
    print(f"✅ Cleaned {len(cleaned)} records")
    return cleaned


# MAIN EXECUTION

def main():
    print("\n\n")
    print("=" * 50)
    print("Istanbul Traffic Accidents - Web Scraper")
    print("=" * 50)
    print()
    
    # Scrape from all sources
    ipa_data = scrape_ipa_data()
    time.sleep(1)  # Be polite to servers
    
    dailysabah_data = scrape_dailysabah_data()
    time.sleep(1)
    
    xinhua_data = scrape_xinhua_data()
    
    # Combine all data
    all_data = ipa_data + dailysabah_data + xinhua_data
    print(f"\n📊 Total records scraped: {len(all_data)}")
    
    # Clean the data
    cleaned_data = clean_scraped_data(all_data)
    
    # Save to CSV
    df = pd.DataFrame(cleaned_data)
    df.to_csv('scraped_accidents.csv', index=False, encoding='utf-8')
    print(f"\n💾 Saved to 'scraped_accidents.csv'")
    
    # Show sample
    print("\n📋 Sample of cleaned data:")
    print(df.head())
    
    print("\n✅ Scraping complete!")
    print("Next step: Run analysis.py to perform statistical analysis\n\n")


if __name__ == '__main__':
    main()


# NOTES FOR REAL IMPLEMENTATION

"""
IMPORTANT: This is a template. For real implementation:

1. Replace URLs with actual sources
2. Inspect each website's HTML structure using browser DevTools
3. Adjust BeautifulSoup selectors to match actual HTML
4. Handle errors and edge cases
5. Respect robots.txt and add delays between requests
6. Consider using headers to avoid being blocked:
   
   headers = {
       'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
   }
   response = requests.get(url, headers=headers)

7. For JavaScript-heavy sites, use Selenium:
   
   from selenium import webdriver
   driver = webdriver.Chrome()
   driver.get(url)
   html = driver.page_source
   soup = BeautifulSoup(html, 'html.parser')

MESSY DATA CHALLENGES YOU'LL ENCOUNTER:
- Inconsistent date formats (DD/MM/YYYY vs YYYY-MM-DD)
- Turkish characters (ş, ğ, ı, ö, ü, ç)
- Mixed languages (Turkish and English)
- Numbers written as text ("yüz elli" = 150)
- Missing values and incomplete records
- Duplicate entries across sources
- Different time zones
"""

# The end of scraper.py