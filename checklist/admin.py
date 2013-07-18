from django.contrib import admin

# import app models
#from checklist import models as cl
#from checklist.models import ReviewChecklist
from checklist.models import Checklist
from checklist.models import Item
from checklist.models import PlanTitle
from checklist.models import MainBody
from checklist.models import Scenery
from checklist.models import DepositStatement
from checklist.models import IntegratedSurveyArea
from checklist.models import Miscellanous
from checklist.models import ElectronicPlan

#from checklist.models import SimpleForm


# Inline classes for checklist items separated into sections
class ItemInline(admin.TabularInline):
    model = Item
    extra = 0
    
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
        (None,               {'fields': ['status']}),
        (None,               {'fields': ['assignee']}),
        (None,               {'fields': ['fileNum']}),
        (None,               {'fields': ['title']}),
        (None,               {'fields': ['description']}),                
        (None,               {'fields': ['create_date']}),
        (None,               {'fields': ['landDistrict']}),
        (None,               {'fields': ['address']}),
    ]
    inlines = [ItemInline]
    #inlines = [ItemInline,PlanTitleInline,MainBodyInline,SceneryInline,DepositStatementInline,IntegratedSurveyAreaInline,MiscellanousInline,ElectronicPlanInline]
    list_display = ('title', 'assignee', 'landDistrict', 'create_date', 'status')
    list_filter = ['status', 'assignee', 'landDistrict', 'create_date']
    search_fields = ['title', 'assignnee']
    date_hierarchy = 'create_date'

# Registering models to Admin page with ModleAdmin format (in this case Checklist and ChecklistAdmin)
# All models that wish to be displayed in Admin page need to be registered
# and all attributes that wish to be displayed in a model need to be in the ModelAdmin form
admin.site.register(Checklist, ChecklistAdmin)




# Modifying default UserAdmin behaviour to restrict 'add user' and 'change user' permission
# not to let anyone but SuperUser to add or update SuperUser status
# This is to avoid non-superuser to create superuser or to update them to super user (or add more permission to themselve)
# One drawback is to create new manager or admin, they have to be super user

from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

class MyUserAdmin(UserAdmin):
    def queryset(self,request):
        qs = admin.ModelAdmin.queryset(self,request)
        if request.user.is_superuser:
            return qs
        # Only allow viewing/editing users who are not superusers
        return qs.filter(is_superuser=False)
    def get_readonly_fields(self, request, obj=None):
        # Deny editing groups, permissions and the superuser status
        return () if request.user.is_superuser else ('is_superuser', 'groups', 'user_permissions')

admin.site.unregister(User)
admin.site.register(User, MyUserAdmin)
