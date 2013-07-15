from django.contrib import admin

# import app models
#from checklist import models as cl
from checklist.models import Checklist
from checklist.models import PlanTitle
from checklist.models import MainBody
from checklist.models import Scenery
from checklist.models import DepositStatement
from checklist.models import IntegratedSurveyArea
from checklist.models import Miscellanous
from checklist.models import ElectronicPlan


from checklist.models import Student
#from checklist.models import SimpleForm


# Inline classes for checklist items separated into sections
class PlanTitleInline(admin.TabularInline):
    model = PlanTitle
    extra = 0

class MainBodyInline(admin.TabularInline):
    model = MainBody
    extra = 0

class SceneryInline(admin.TabularInline):
    model = Scenery
    extra = 0

class DepositStatementInline(admin.TabularInline):
    model = DepositStatement
    extra = 0

class IntegratedSurveyAreaInline(admin.TabularInline):
    model = IntegratedSurveyArea
    extra = 0

class MiscellanousInline(admin.TabularInline):
    model = Miscellanous
    extra = 0

class ElectronicPlanInline(admin.TabularInline):
    model = ElectronicPlan
    extra = 0

class ChecklistAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['fileNum']}),
        (None,               {'fields': ['title']}),
        (None,               {'fields': ['description']}),                
        #('Date information', {'fields': ['create_date'], 'classes': ['collapse']}),
        (None,               {'fields': ['create_date']}),
        (None,               {'fields': ['landDistrict']}),
        (None,               {'fields': ['address']}),
    ]
    inlines = [PlanTitleInline,MainBodyInline,SceneryInline,DepositStatementInline,IntegratedSurveyAreaInline,MiscellanousInline,ElectronicPlanInline]
    list_display = ('title', 'create_date', 'was_created_today')
    list_filter = ['title', 'landDistrict', 'create_date']
    search_fields = ['title']
    date_hierarchy = 'create_date'

   
admin.site.register(Checklist, ChecklistAdmin)
#admin.site.register(PlanTitle)
admin.site.register(Student)
#admin.site.register(SimpleForm)
