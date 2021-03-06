from django.contrib import admin

from django.forms.widgets import CheckboxSelectMultiple

# import app models
from checklist.models import Checklist, Item, ChecklistForm

# Inline classes for formatting display of One-to-Many relationship
class ItemInline(admin.TabularInline):
    model = Item
    extra = 0
    
# ModelAdmin classes for specifying how a Model is being displayed and structured on Admin page
class ChecklistAdmin(admin.ModelAdmin):
    # User filter horizontal field to display pretty 'SelectMultiple' widgets, namely for ManyToManyField attribute
    filter_horizontal = ('assignees',)
	
	# Using 'form' field is another way to override default widgets, defined in ChecklistForm in Model
    #form = ChecklistForm
	
	# Dictate which attribute to be shown in which format and order
    fieldsets = [
    	(None, {'fields': ('status','assignees','fileNum','title','description','create_date','landDistrict','address','comment')}),
    ]

    inlines = [ItemInline]
    list_display = ('title', 'assigner', 'assignee_names', 'landDistrict', 'create_date', 'status')
    list_filter = ['status', 'assigner', 'assignees', 'landDistrict', 'create_date']
    search_fields = ['title', 'assigner', 'assignnees']
    date_hierarchy = 'create_date'
    
    # Override ModelAdmin save_model function to save request user as creator of new checklist
    def save_model(self, request, obj, form, change):
		"""When creating a new object, set the creator field.
		"""
		if not change:
		    obj.assigner = request.user
		obj.save()

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
