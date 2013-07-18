from django.db import models
from django.contrib.auth.models import User as AutUser

# wiget forms for html submittion (for surveyor live_checklist later and also for 'review_checklist')
from django import forms
from django.forms.widgets import RadioSelect, CheckboxSelectMultiple

import datetime


# Create your models here.
"""
class ReviewChecklist(models.Model):
	fileNum = ""
	title = ""
	description = ""
	create_date = ""
	landDistrict = ""
	address = ""
	assignee = models.ForeignKey(AutUser, blank=True, null=True)
	APPROVE_CHOICES = (
		('A', 'Approved'),
		('R', 'Rejected'),
	)
	is_approved = models.CharField(max_length=1,choices=APPROVE_CHOICES,default='R')
	
	def __unicode__(self):
		return self.title
"""
class Checklist(models.Model):
	fileNum = models.CharField(max_length=20)
	title = models.CharField(max_length=100)
	description = models.CharField(max_length=500)
	create_date = models.DateTimeField('date created')
	landDistrict = models.CharField(max_length=100)
	address = models.CharField(max_length=100)
	assignee = models.ForeignKey(AutUser, blank=True, null=True)
	STATUS_CHOICES = (
		('N', 'New'),
		('I', 'Inprogress'),
		('S', 'Submited'),
		('A', 'Approved'),
		('R', 'Rejected'),
	)
	status = models.CharField(max_length=1,choices=STATUS_CHOICES,default='N')
	
	def __unicode__(self):
		return self.title
	def was_created_today(self):
		return self.pub_date.date() == datetime.date.today()
	was_created_today.short_description = 'Created today?'

class Item(models.Model):
	checklist = models.ForeignKey(Checklist)
	TYPE_CHOICES = (
		('PT', 'Plan Title'),
		('MB', 'Main Body'),
		('S', 'Scenery'),
		('DS', 'Deposit Statement'),
		('ISA', 'Integrated Survey Area'),
		('M', 'Miscellanous'),
		('EP', 'Electronic Plan'),
	)
	itemType = models.CharField(max_length=5,choices=TYPE_CHOICES,default='PT')
	item = models.CharField(max_length=100)
	STATUS_CHOICES = (
		('U', 'Unanswered'),
		('Y', 'Yes'),
		('N', 'N/A'),
	)	
	itemStatus = models.CharField(max_length=2,choices=STATUS_CHOICES,default='U')

	def __unicode__(self):
		return self.item	

	#def is_upperclass(self):
	#	return self.year_in_school in (self.JUNIOR, self.SENIOR)
	
class PlanTitle(models.Model):
	checklist = models.ForeignKey(Checklist)
	item = models.CharField(max_length=100)
	def __unicode__(self):
		return self.item

class MainBody(models.Model):
	checklist = models.ForeignKey(Checklist)
	item = models.CharField(max_length=100)
	def __unicode__(self):
		return self.item

class Scenery(models.Model):
	checklist = models.ForeignKey(Checklist)
	item = models.CharField(max_length=100)
	def __unicode__(self):
		return self.item

class DepositStatement(models.Model):
	checklist = models.ForeignKey(Checklist)
	item = models.CharField(max_length=100)
	def __unicode__(self):
		return self.item

class IntegratedSurveyArea(models.Model):
	checklist = models.ForeignKey(Checklist)
	item = models.CharField(max_length=100)
	def __unicode__(self):
		return self.item

class Miscellanous(models.Model):
	checklist = models.ForeignKey(Checklist)
	item = models.CharField(max_length=100)
	def __unicode__(self):
		return self.item
		
class ElectronicPlan(models.Model):
	checklist = models.ForeignKey(Checklist)
	item = models.CharField(max_length=100)
	def __unicode__(self):
		return self.item
		

		
"""
from django.forms.fields import DateField, ChoiceField, MultipleChoiceField
from django.forms.widgets import RadioSelect, CheckboxSelectMultiple
from django.forms.extras.widgets import SelectDateWidget

BIRTH_YEAR_CHOICES = ('1980', '1981', '1982')
FAVORITE_COLORS_CHOICES = (('blue', 'Blue'),
							('green', 'Green'),
							('black', 'Black'))

class SimpleForm(forms.Form):
	birth_year = DateField(widget=SelectDateWidget(years=BIRTH_YEAR_CHOICES))
	favorite_colors = forms.MultipleChoiceField(required=False,
		widget=CheckboxSelectMultiple, choices=FAVORITE_COLORS_CHOICES)
"""
