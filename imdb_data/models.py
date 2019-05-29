from django.db import models
from multiselectfield import MultiSelectField

# Create your models here.

GENRE_CHOICES = (
    ('Action', 'Action'),
	('Adult', 'Adult'),
	('Adventure', 'Adventure '),
	('Animation', 'Animation'),
	('Biography', 'Biography'),
	('Comedy', 'Comedy'),
	('Crime', 'Crime'),
	('Documentary', 'Documentary'),
	('Drama', 'Drama'),
	('Family', 'Family'),
	('Fantasy', 'Fantasy'),
	('Film Noir', 'Film Noir'),
	('Game-Show', 'Game-Show'),
	('History', 'History'),
	('Horror', 'Horror'),
	('Musical', 'Musical'),
	('Music', 'Music'),
	('Mystery', 'Mystery'),
	('News', 'News'),
	('Reality-TV', 'Reality-TV'),
	('Romance', 'Romance'),
	('Sci-Fi', 'Sci-Fi'),
	('Short', 'Short'),
	('Sport', 'Sport'),
	('Talk-Show', 'Talk-Show'),
	('Thriller', 'Thriller'),
	('War', 'War'),
	('Western', 'Western'),
)

class imdb_data(models.Model):
	name = models.CharField(max_length=150)
	director = models.CharField(max_length=150)
	imdb_score = models.FloatField(null=True, blank=True)
	genre = MultiSelectField(choices=GENRE_CHOICES)
	popularity = models.FloatField(null=True, blank=True)

	def __str__(self):
		return self.name