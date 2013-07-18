from django.db import models
from django.contrib.auth.models import User as AutUser

# wiget forms for html submittion (for surveyor live_checklist later and also for 'review_checklist')
from django import forms
from django.forms.widgets import RadioSelect, CheckboxSelectMultiple

import datetime


# Create your models here.

# Database model for Checklist
# Checklist is associated with AuthUser as Many-to-One relationship
# Checklist also has implicit One-to-Many relationship with Item model
# Each checklist has status of 'New', 'Inprogress', 'Submited', 'Approved', or 'Rejected'
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

# Database model for Item in the checklist
# Item has many-to-one relationship with Checklist
# Each item has status of 'Unanswered', 'Yes', or 'N/A'
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


# Extra experimental database models for separate sections of an item
# May not be needed as this complicates things
# The only benefit is it looks nicer on the Admin manager page where each subsection has its own section	
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
	

		

