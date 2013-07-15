from django.db import models
from django import forms
from django.forms.widgets import RadioSelect, CheckboxSelectMultiple

import datetime


# Create your models here.
class Checklist(models.Model):
	fileNum = models.CharField(max_length=20)
	title = models.CharField(max_length=100)
	description = models.CharField(max_length=500)
	create_date = models.DateTimeField('date created')
	landDistrict = models.CharField(max_length=100)
	address = models.CharField(max_length=100)
	#assigner = 
	#assignee = models.ForeignKey(auth_user, blank=True, null=True)
	
	def __unicode__(self):
		return self.title
	def was_created_today(self):
		return self.pub_date.date() == datetime.date.today()
	was_created_today.short_description = 'Created today?'

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
		
class Student(models.Model):
    FRESHMAN = 'FR'
    SOPHOMORE = 'SO'
    JUNIOR = 'JR'
    SENIOR = 'SR'
    YEAR_IN_SCHOOL_CHOICES = (
        (FRESHMAN, 'Freshman'),
        (SOPHOMORE, 'Sophomore'),
        (JUNIOR, 'Junior'),
        (SENIOR, 'Senior'),
    )
    year_in_school = models.CharField(max_length=2,
                                      choices=YEAR_IN_SCHOOL_CHOICES,
                                      default=FRESHMAN)

    def is_upperclass(self):
        return self.year_in_school in (self.JUNIOR, self.SENIOR)
        
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
