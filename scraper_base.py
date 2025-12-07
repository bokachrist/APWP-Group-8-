from abc import ABC, abstractmethod
from typing import List, Protocol
from models import Movie

class Scraper(ABC):

    @abstractmethod
    def scrape(self) -> List[Movie]:
        pass

    @abstractmethod
    def get_source_name(self) -> str:
        pass


class DatabaseProtocol(Protocol):

    def save_movie(self, movie: Movie) -> bool: ...
    def get_all_movies(self) -> List[Movie]: ...
    def search_by_title(self, title: str) -> List[Movie]: ...

# End of scraper_base.py(2)
