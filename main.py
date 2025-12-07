from database import MongoDBManager
from manager import MovieManager
from imdb_scraper import IMDbScraper
# from tmdb_scraper import TMDbAPIScraper  # optional

def main():

    print("\n\n\n                                                             Welcome to the Top 10 Movie Scraper Project!\n\n\n🎬 Movie Database Manager")
    print("="*50)

    try:
        db = MongoDBManager()
        manager = MovieManager(db)

        manager.add_scraper(IMDbScraper(limit=15))
        # manager.add_scraper(TMDbAPIScraper(limit=10))

        manager.scrape_and_save()
        manager.display_statistics()
        manager.show_top_movies(10)

        db.close()
        print("\n✅ Application completed successfully!")

    except Exception as e:
        print(f"\n❌ Application error: {e}")


if __name__ == "__main__":
    main()

print("==================================================")
print("\n\n\n                                                                     All tasks completed!\n\n\n")

# End of main.py(7)
