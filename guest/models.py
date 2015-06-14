# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import datetime
from django.db import models
from django.utils import timezone


class Agent(models.Model):
	name = models.CharField(max_length=200)
	is_banned = models.BooleanField(default=False)
	def __str__(self):              # __unicode__ on Python 2
		return self.name

class Record(models.Model):
	agent = models.ForeignKey(Agent)
	department = models.CharField(max_length=5)
	grade = models.CharField(max_length=1)
	phone = models.CharField(max_length=15)
	start_date = models.DateTimeField('借用日期')
	end_date = models.DateTimeField('歸還日期', null=True)
	number_of_days = models.IntegerField()
	identification = models.CharField(max_length = 5)
	person_in_charge = models.CharField(max_length = 4)
	is_deleted = models.BooleanField(default=False)
	def __str__(self):
		# print(self.item_set)
		return '由%s來自%s %s所借%s個' % (self.agent.name, self.department, self.grade, ",".join([e.__str__() for e in self.item_set.all()]))


class Item(models.Model):
	number = models.IntegerField()
	Record = models.ForeignKey(Record)
	ItemType = models.ForeignKey('ItemType')
	def __str__(self):              # __unicode__ on Python 2
		return "%s x%d" % (self.ItemType.Item_text,self.number)

class ItemType(models.Model):
	Item_text = models.CharField(max_length=20)
	def __str__(self):
		return self.Item_text








