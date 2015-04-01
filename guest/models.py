import datetime

from django.db import models
from django.utils import timezone



class Item(models.Model):
	interval_options = (
		('hours', 'hours'),
		('one_week', '一週'),
		('one_day', '一天')
		)
	Item_text = models.CharField(max_length=200)
	interval = models.CharField(max_length=200)
	def __str__(self):              # __unicode__ on Python 2
		return self.Item_text
	pub_date = models.DateTimeField('date published')
	def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Agent(models.Model):
	name = models.CharField(max_length=200)
	is_banned = models.BooleanField(default=True)
	def __str__(self):              # __unicode__ on Python 2
		return self.name

class Record(models.Model):
	item = models.ForeignKey(Item)
	start = models.DateTimeField('start_time')
	end = models.DateTimeField('end_time')
	agent = models.ForeignKey(Agent)
	is_deleted = models.BooleanField(default=True)


