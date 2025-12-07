from typing import List
from scraper_base import Scraper
from database import MongoDBManager
from models import Movie

class MovieManager:

    def __init__(self, db_manager: MongoDBManager):
        self.db = db_manager
        self.scrapers: List[Scraper] = []

    def add_scraper(self, scraper: Scraper):
        self.scrapers.append(scraper)

    def scrape_and_save(self):
        print("\n" + "="*50)
        print("Starting Movie Scraping Process")
        print("="*50)

        for scraper in self.scrapers:
            print(f"\n📡 Scraping from: {scraper.get_source_name()}")
            movies = scraper.scrape()
            print(f"   Found {len(movies)} movies")

            saved = self.db.save_movies(movies)
            print(f"   Saved {saved} new movies to database")

    def display_statistics(self):
        all_movies = self.db.get_all_movies()
        print("\n" + "="*50)
        print("Database Statistics")
        print("="*50)
        print(f"Total movies in database: {len(all_movies)}")

        if all_movies:
            avg_rating = sum(m.rating for m in all_movies) / len(all_movies)
            print(f"Average rating: {avg_rating:.2f}")

    def show_top_movies(self, limit=10):
        print("\n" + "="*50)
        print(f"Top {limit} Rated Movies")
        print("="*50)

        top = self.db.get_top_rated(limit)

        for i, movie in enumerate(top, 1):
            print(f"{i}. {movie.title} ({movie.year}) - ⭐ {movie.rating}")
            print("\n")

# End of manager.py(6)
