import requests
from typing import List
from models import Movie
from scraper_base import Scraper

class TMDbAPIScraper(Scraper):

    def __init__(self, limit: int = 20):
        self.limit = limit
        self.api_key = "your_api_key_here"
        self.base_url = "https://api.themoviedb.org/3"

    def scrape(self) -> List[Movie]:
        try:
            url = f"{self.base_url}/movie/popular"
            params = {'api_key': self.api_key, 'language': 'en-US', 'page': 1}

            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()

            movies = []

            for item in data.get('results', [])[:self.limit]:
                movies.append(
                    Movie(
                        title=item.get('title', 'Unknown'),
                        year=int(item.get('release_date', '2024')[:4]) if item.get('release_date') else 2024,
                        rating=float(item.get('vote_average', 0.0)),
                        genres=[str(g) for g in item.get('genre_ids', [])],
                        url=f"https://www.themoviedb.org/movie/{item.get('id', '')}"
                    )
                )

            return movies

        except Exception as e:
            print(f"Error fetching from TMDb API: {e}")
            return []

    def get_source_name(self) -> str:
        return "TMDb API"

# End of tmdb_scraper.py(4)
