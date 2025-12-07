# 🎬 Movie Database Manager

A Python application that scrapes movie data from IMDB and TMDB. Then stores it in MongoDB with full OOP implementation.

## 📋 Project Overview

This project demonstrates web scraping, API integration, database management, and object-oriented programming principles by building a movie database manager that:
- Scrapes movie data from IMDb using BeautifulSoup
- Fetches data from TMDb API (optional)
- Stores data in MongoDB
- Provides querying and analysis capabilities

## 🎯 Features Implemented

### Web Scraping & APIs
- ✅ **BeautifulSoup (bs4)** - Scraping IMDb Top 250 movies
- ✅ **Standard APIs** - TMDb API integration (optional)
- ⚡ Upgradeable to Selenium/Scrapy for advanced scraping

### Database
- ✅ **MongoDB** - NoSQL database for flexible movie storage
- ✅ Unique indexing on movie titles
- ✅ CRUD operations with error handling

### Business Logic & OOP
- ✅ **Classes** - Multiple well-structured classes
- ✅ **Inheritance** - `Scraper` base class with multiple implementations
- ✅ **Abstract Classes** - `ABC` for scraper blueprint
- ✅ **Protocols** - `DatabaseProtocol` for type checking
- ✅ **Data Classes** - `Movie` dataclass with field defaults
- ✅ **Full Type Checking** - Type hints throughout the codebase
- ✅ **ORM Pattern** - Database manager with object mapping

## 🏆 Bonus Points Achieved

| Category | Implementation | Points |
|----------|---------------|---------|
| **Web Scraping** | BeautifulSoup + API | Base + 0 (20 optional) |
| **Database** | MongoDB | Base + 15 |
| **OOP** | Data classes + Type checking + ORM | Base + 15 |
| **Total Bonus** | | **+30** |

## 📁 Project Structure

```
project2&3(movie_scraper)/
├── models.py
├── scraper_base.py
├── imdb_scraper.py
├── tmdb_scraper.py
├── database.py
├── manager.py
├── main.py
├── README.md
├── gtignore.txt
└── requirements.txt
__pycache__/
├── database.cpython-314.pyc
├── imdb_scrapercpython-314.pyc
├── manager.cpython-314.pyc
├── models.cpython-314.pyc
├── movie.cpython-314.pyc
└── scraper_base.cpython-314.pyc
```

## 🚀 Installation & Setup

### Prerequisites
- Python 3.8 or higher
- MongoDB installed and running locally
- (Optional) TMDb API key for additional data source

### Step 1: Install MongoDB

**Windows:**
```bash
# Download from: https://www.mongodb.com/try/download/community
# Install and start MongoDB service
```

**macOS:**
```bash
brew tap mongodb/brew
brew install mongodb-community
brew services start mongodb-community
```

**Linux:**
```bash
sudo apt-get install mongodb
sudo systemctl start mongodb
```

### Step 2: Clone and Setup

```bash
# Clone the repository
git clone <your-repo-url>
cd movie-database-manager

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Step 3: (Optional) Get TMDb API Key

1. Create free account at https://www.themoviedb.org/
2. Go to Settings > API
3. Request API key

### Step 4: Run the Application

```bash
python main.py
```

## 💻 Usage

The application automatically:
1. Connects to MongoDB
2. Scrapes movie data from IMDb
3. Saves movies to database (avoiding duplicates)
4. Displays statistics and top-rated movies

### Sample Output

```
Welcome to the Top 10 Movive Scraper Project!


🎬 Movie Database Manager
==================================================
✅ Connected to MongoDB: movies_db

==================================================
Starting Movie Scraping Process
==================================================

📡 Scraping from: IMDb Top 250
   Found 15 movies
Movie 'The Shawshank Redemption' already exists
Movie 'The Godfather' already exists
Movie 'The Dark Knight' already exists
Movie 'The Godfather Part II' already exists
Movie '12 Angry Men' already exists
Movie 'The Lord of the Rings: The Return of the King' already exists
Movie 'Schindler's List' already exists
Movie 'The Lord of the Rings: The Fellowship of the Ring' already exists
Movie 'Pulp Fiction' already exists
Movie 'Il buono, il brutto, il cattivo' already exists
Movie 'The Lord of the Rings: The Two Towers' already exists
Movie 'Forrest Gump' already exists
Movie 'Fight Club' already exists
Movie 'Inception' already exists
Movie 'Star Wars: Episode V - The Empire Strikes Back' already exists
   Saved 0 new movies to database

==================================================
Database Statistics
==================================================
Total movies in database: 15
Average rating: 8.93

==================================================
Top 10 Rated Movies
==================================================
1. The Shawshank Redemption (1994) - ⭐ 9.3


2. The Godfather (1972) - ⭐ 9.2


3. The Dark Knight (2008) - ⭐ 9.1
...
```

## 🔧 Code Highlights

### Data Classes with Type Checking
```python
@dataclass
class Movie:
    title: str
    year: int
    rating: float
    genres: List[str] = field(default_factory=list)
```

### Abstract Base Class
```python
class Scraper(ABC):
    @abstractmethod
    def scrape(self) -> List[Movie]:
        pass
```

### Protocol for Type Safety
```python
class DatabaseProtocol(Protocol):
    def save_movie(self, movie: Movie) -> bool:
        ...
```

### ORM-like Database Pattern
```python
class MongoDBManager:
    def save_movie(self, movie: Movie) -> bool:
        return self.collection.insert_one(movie.to_dict())
```

## 🎓 Learning Outcomes

This project demonstrates understanding of:
- Web scraping techniques and ethics
- API integration and error handling
- NoSQL database operations
- Object-oriented design principles
- Python type hints and protocols
- Clean code architecture
- Error handling and robustness

## 📦 Dependencies

- `requests` - HTTP library for web scraping and API calls
- `beautifulsoup4` - HTML parsing library
- `pymongo` - MongoDB driver for Python
- `lxml` - Fast XML/HTML parser

### Bonus Points Breakdown:

1. **Database (+15)**
   - Using MongoDB (NoSQL database)
   - Proper connection handling
   - CRUD operations implemented

2. **OOP (+15)**
   - ✅ Classes used throughout
   - ✅ Inheritance (Scraper → IMDbScraper, TMDbAPIScraper)
   - ✅ Abstract base class (Scraper with ABC)
   - ✅ Protocol (DatabaseProtocol)
   - ✅ Data classes with defaults
   - ✅ Full type checking (Type hints on all functions/methods)
   - ✅ ORM pattern in database manager

3. **Web Scraping (Base)**
   - BeautifulSoup for IMDb
   - Requests for API calls
   - Proper error handling

### Code Quality:
- Clean, readable code with comments
- Follows Python naming conventions
- Error handling throughout
- Type safety with protocols and hints
- Modular design with clear separation of concerns

## 👨‍💻 Author

ICT 2nd Year Students - [Iyad Kabel, Y.H.Y.M.Bakr Raiyan, Amro Jamal Al Ddın, Christ Barhith Boka, Muzammal Yaquib]

## 📄 License

This project is created for educational purposes.


