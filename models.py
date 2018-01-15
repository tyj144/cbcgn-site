# Based on https://www.djangorocks.com/tutorials/how-to-create-a-basic-blog-in-django/defining-your-models.html
# remember to register models in admin.py

from django.db import models

# https://github.com/jazzband/django-embed-video
from embed_video.fields import EmbedVideoField

class Event(models.Model):
	'''represents a church event displayed on front page'''
	title = models.CharField(max_length=100, unique=True)
	description = models.TextField()

	slug = models.SlugField(max_length=100, unique=True)
	video = EmbedVideoField(blank=True)

	start_date = models.DateField(db_index=True)
	end_date = models.DateField(db_index=True)

	category = models.ForeignKey('content.Category')

	# returns string equivalent of object (necessary to see things in admin panel)
	def __str__(self):
		return '%s' % self.title

	def get_absolute_url(self):
		return ('view_event', None, { 'slug': self.slug })

class Category(models.Model):
	'''a category for the event (e.g. Youth, Children, Outreach, etc.)'''
	# displays plural of 'category' as 'categories' instead of 'categorys' in the admin panel
	class Meta:
		verbose_name_plural = "categories"

	title = models.CharField(max_length=100, db_index=True)
	slug = models.SlugField(max_length=100, db_index=True)

	def __str__(self):
		return '%s' % self.title

	def get_absolute_url(self):
		return ('view_event_category', None, { 'slug': self.slug })

class Sermon(models.Model):
	'''a way of storing sermons (only by url, not by mp3 file)'''
	date = models.DateField(db_index=True)
	title = models.CharField(max_length=100, db_index=True)

	# eventually need to find a way to store and link audio locally
	url = models.URLField(max_length=200)

	def __str__(self):
		return '%s' % self.title