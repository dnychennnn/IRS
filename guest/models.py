from django.db import models

class Item(models.Model):
	Item_text = models.CharField(max_length=200)
	iterval = models.DateField()

class Record(models.Model)
	item = models.ForeignKey('Item')
	start = models.DateTimeField('start_time')
	end = models.DateTimeField('end_time')
	agent = models.ForeignKey('Agent')
	is_deleted = models.BooleanField()

class Agent(models.Model)
	record = models.ForeignKey('Record')
	name = models.CharField('agent')
	is_banned = models.BooleanField()
