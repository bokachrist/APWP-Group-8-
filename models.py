from dataclasses import dataclass, field
from datetime import datetime
from typing import List

@dataclass
class Movie:
    title: str
    year: int
    rating: float
    genres: List[str] = field(default_factory=list)
    url: str = ""
    scraped_at: datetime = field(default_factory=datetime.now)

    def to_dict(self) -> dict:
        return {
            'title': self.title,
            'year': self.year,
            'rating': self.rating,
            'genres': self.genres,
            'url': self.url,
            'scraped_at': self.scraped_at
        }

# End of models.py(1)
