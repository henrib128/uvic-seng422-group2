from django.contrib import admin

# import app models
from checklist.models import Checklist
from checklist.models import PlanTitle
from checklist.models import Student
#from checklist.models import SimpleForm



class PlanTitleInline(admin.TabularInline):
    model = PlanTitle
    extra = 2
      
class ChecklistAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['fileNum']}),
        (None,               {'fields': ['title']}),
        (None,               {'fields': ['description']}),                
        ('Date information', {'fields': ['create_date'], 'classes': ['collapse']}),
        (None,               {'fields': ['landDist']}),
        (None,               {'fields': ['address']}),
    ]
    inlines = [PlanTitleInline]
    list_display = ('title', 'create_date', 'was_created_today')
    list_filter = ['title', 'landDist', 'create_date']
    search_fields = ['title']
    date_hierarchy = 'create_date'

class PlanTitleAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['section1']}),
        (None,               {'fields': ['section2']}),
        #('Poll information', {'fields': ['Poll'], 'classes': ['collapse']}),
    ]
    #inlines = [ChoiceInline]
    #list_display = ('section', 'checklist')
    #list_filter = ['question','pub_date']
    
admin.site.register(Checklist, ChecklistAdmin)
admin.site.register(PlanTitle)
admin.site.register(Student)
#admin.site.register(SimpleForm)
