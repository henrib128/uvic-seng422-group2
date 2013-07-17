# Required packages for http response and render
from django.template import Context, loader
from django.core.context_processors import csrf
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, render
from django.core.urlresolvers import reverse

from django.contrib.auth import authenticate, login, logout
#from django.contrib.auth.decorators import login_required

# Database related models
from checklist.models import Checklist
from checklist.models import Item

# Create your view functions here.

# logout view
def logout_view(request):
	logout(request)

def index(request):
	# First logout current user
	#logout_view(request)
	
	# csrf token	
	c = {}
	c.update(csrf(request))
	
	# Call index.html
	return render_to_response('checklist/index.html',c)
	
#@login_required(login_url='/checklist')
def login_view(request):
	# csrf token
	c = {}
	c.update(csrf(request))

	# Extract user login info from indext to login page
	username = request.POST['username']
	password = request.POST['password']
		
	user = authenticate(username=username, password=password)
	if user is not None:
		if user.is_active:
			# Log user in and associate it with current request
			login(request, user) # remember to log user out later!
		
			# Get a list of checklists assigned to this user
			aut_user = request.user
			checklists = aut_user.checklist_set.all().order_by('-create_date')
		
			# Use render() for auto adding request context and csrf, html should refer user as 'user' (not 'request.user')
			return render(request,'checklist/surveyor_home.html', {'checklists': checklists})

			
		else:
			# Return a 'disabled account' error message
			return HttpResponse("Unactive account.",c)
	else:
		# Return an 'invalid login' error message.
		return HttpResponse("Invalid login.",c)

# Function to dislay detail view of a checklist_id 
def checklist_detail(request, checklist_id):
	#p = get_object_or_404(Poll, pk=poll_id)
	checklist = Checklist.objects.get(id=checklist_id)
	return render(request,'checklist/checklist_detail.html', {'checklist': checklist})


# Function to update items status of checklist 
def checklist_save(request, checklist_id):
	#p = get_object_or_404(Poll, pk=poll_id)
	checklist = Checklist.objects.get(id=checklist_id)
	try:
		selected_choice = request.POST['choice']
		item_id = request.POST['item'].strip('/')
		#return HttpResponse("Item id: %s and choice: %s" % (item_id,selected_choice))
		selected_item = checklist.item_set.get(id=item_id)

	except (KeyError, Item.DoesNotExist):
		# Redisplay the poll voting form.
		return render(request,'checklist/checklist_detail.html', {'checklist': checklist, 'error_message': "You didn't select a choice."})	
	else:
		# Save selected choice to database
		selected_item.itemStatus = selected_choice
		selected_item.save()
		# Always return an HttpResponseRedirect after successfully dealing
		# with POST data. This prevents data from being posted twice if a
		# user hits the Back button.
		return HttpResponseRedirect(reverse('checklist.views.checklist_result', args=(checklist.id,)))
		
		
# Function to display checklist result
def checklist_result(request, checklist_id):
	checklist = Checklist.objects.get(id=checklist_id)
	return render(request,'checklist/checklist_result.html', {'checklist': checklist})
	   
	
	
	
