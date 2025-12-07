from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError
from datetime import datetime
from typing import List
from models import Movie

class MongoDBManager:

    def __init__(self, connection_string="mongodb://localhost:27017/", database_name="movies_db"):
        try:
            self.client = MongoClient(connection_string)
            self.db = self.client[database_name]
            self.collection = self.db['movies']
            self.collection.create_index('title', unique=True)
            print(f"✅ Connected to MongoDB: {database_name}")
        except Exception as e:
            print(f"❌ MongoDB connection failed: {e}")
            raise

    def save_movie(self, movie: Movie) -> bool:
        try:
            self.collection.insert_one(movie.to_dict())
            return True
        except DuplicateKeyError:
            print(f"Movie '{movie.title}' already exists")
            return False
        except Exception as e:
            print(f"Error saving movie: {e}")
            return False

    def save_movies(self, movies: List[Movie]) -> int:
        saved = 0
        for movie in movies:
            if self.save_movie(movie):
                saved += 1
        return saved

    def get_all_movies(self) -> List[Movie]:
        movies = []
        for doc in self.collection.find():
            movies.append(Movie(
                title=doc['title'],
                year=doc['year'],
                rating=doc['rating'],
                genres=doc.get('genres', []),
                url=doc.get('url', ''),
                scraped_at=doc.get('scraped_at', datetime.now())
            ))
        return movies

    def search_by_title(self, title: str) -> List[Movie]:
        query = {'title': {'$regex': title, '$options': 'i'}}
        return [
            Movie(doc['title'], doc['year'], doc['rating'], doc.get('genres', []), doc.get('url', ''))
            for doc in self.collection.find(query)
        ]

    def get_top_rated(self, limit: int = 10) -> List[Movie]:
        return [
            Movie(doc['title'], doc['year'], doc['rating'], doc.get('genres', []), doc.get('url', ''))
            for doc in self.collection.find().sort('rating', -1).limit(limit)
        ]

    def close(self):
        self.client.close()

# End of database.py(5)
