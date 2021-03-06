# Import Django classes for models
from django.db import models
from django.contrib.auth.models import User as AutUser

# Packages to customize ModelForm, for instance changing default value of widget for each field type
from django.forms import ModelForm
from django.forms.widgets import CheckboxSelectMultiple

#################################################### Create your models here.

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
	assigner = models.ForeignKey(AutUser, related_name='checklist_assigner', blank=True, null=True)
	assignees = models.ManyToManyField(AutUser, related_name='checklist_assignees', blank=True, null=True)
	comment = models.CharField(max_length=100, blank=True)
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

	def assignee_names(self):
		return ', '.join([assignee.username for assignee in self.assignees.all()])
	
	assignee_names.short_description = "Assignees"

# ModelForm class to go with Model class into ModelAdmin's form. This is to override default widget type for certain
# attribute of the Model, for example we want assignees to be displayed as 'CheckboxSelectMultiple' instead of
# default widget as 'select'. So here how you change the meta of the form, especially the widgets meta.
class ChecklistForm(ModelForm):
	class Meta:
		model = Checklist
		widgets = {
            'assignees': CheckboxSelectMultiple
        }

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
	itemComment = models.CharField(max_length=100, blank=True)

	def __unicode__(self):
		return self.item	




