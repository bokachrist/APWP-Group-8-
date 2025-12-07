import requests
from bs4 import BeautifulSoup
from typing import List
from models import Movie
from scraper_base import Scraper

class IMDbScraper(Scraper):

    def __init__(self, limit: int = 20):
        self.limit = limit
        self.base_url = "https://www.imdb.com/chart/top/"

    def scrape(self) -> List[Movie]:
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            }
            response = requests.get(self.base_url, headers=headers, timeout=10)
            response.raise_for_status()

            soup = BeautifulSoup(response.content, 'html.parser')
            movies = []

            movie_items = soup.select('li.ipc-metadata-list-summary-item')[:self.limit]

            for item in movie_items:
                try:
                    title_elem = item.select_one('h3.ipc-title__text')
                    if not title_elem:
                        continue
                    title = title_elem.text.strip().split('. ', 1)[-1]

                    metadata = item.select_one('span.cli-title-metadata-item')
                    year = int(metadata.text.strip()) if metadata else 2024

                    rating_elem = item.select_one('span.ipc-rating-star--rating')
                    rating = float(rating_elem.text.strip()) if rating_elem else 0.0

                    link_elem = item.select_one('a.ipc-title-link-wrapper')
                    url = f"https://www.imdb.com{link_elem['href']}" if link_elem else ""

                    movies.append(Movie(title, year, rating, ['Unknown'], url))

                except Exception as e:
                    print(f"Error parsing movie: {e}")

            return movies

        except Exception as e:
            print(f"Error fetching data: {e}")
            return []

    def get_source_name(self) -> str:
        return "IMDb Top 250"

# End of imdb_scraper.py(3)
