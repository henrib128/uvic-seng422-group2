# Required packages for http response and render
from django.template import Context, loader
from django.core.context_processors import csrf
from django.http import HttpResponse
from django.shortcuts import render_to_response, render

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Database related models
from checklist.models import Checklist

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
		
			# Use render() for auto adding request context, html should refer user as 'user' (not 'request.user')
			#return render(request,'checklist/surveyor_home.html', c)
			return render(request,'checklist/surveyor_home.html', {'checklists': checklists})

			
		else:
			# Return a 'disabled account' error message
			return HttpResponse("Unactive account.",c)
	else:
		# Return an 'invalid login' error message.
		return HttpResponse("Invalid login.",c)
		
  
