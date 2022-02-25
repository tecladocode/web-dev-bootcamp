from dataclasses import dataclass, field
from datetime import datetime
from uuid import uuid4


@dataclass
class Movie:
    _id: str
    title: str
    director: str
    year: int
    cast: list[str] = field(default_factory=lambda: [])
    series: list[str] = field(default_factory=lambda: [])
    last_watched: datetime = None
    rating: int = 0
    tags: list[str] = field(default_factory=lambda: [])
    description: str = None
    video_link: str = None
