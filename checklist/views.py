# Required packages for http response and render
#from django.template import Context, loader
#from django.core.context_processors import csrf
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, render
from django.core.urlresolvers import reverse

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Database related models
from checklist.models import Checklist
from checklist.models import Item



#################################################### Create your view functions here.

# Function to display front page with login option
def index(request):
	# Call index.html
	return render(request, 'checklist/index.html')

# Function to perform logout and redisplay front page
def logout_view(request):
	logout(request)
	message = "You have been logged out."
	return render(request, 'checklist/index.html', {'message' : message})

# Function to perform login and redirect to surveyor home page or front page if invalid login
def login_view(request):
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
			message = "Your account is unactive. Please contact your admin."
			return render(request, 'checklist/index.html', {'message' : message})
	else:
		# Return an 'invalid login' error message.
		message = "Invalid login information!"
		return render(request, 'checklist/index.html', {'message' : message})

# Function to display home view for user, required user to logged in
@login_required(login_url='/checklist/')
def home(request):
	# Get a list of checklists assigned to this user
	aut_user = request.user
	checklists = aut_user.checklist_set.all().order_by('-create_date')

	# Use render() for auto adding request context and csrf, html should refer user as 'user' (not 'request.user')
	return render(request,'checklist/surveyor_home.html', {'checklists': checklists})
		
# Function to dislay detail view of a checklist_id, required user to logged in
@login_required(login_url='/checklist/')
def checklist_detail(request, checklist_id):
	#p = get_object_or_404(Poll, pk=poll_id)
	checklist = Checklist.objects.get(id=checklist_id)
	return render(request,'checklist/checklist_detail.html', {'checklist': checklist})

# Function to update items status of checklist, required user to logged in
@login_required(login_url='/checklist/')
def checklist_save(request, checklist_id):
	#p = get_object_or_404(Poll, pk=poll_id)
	checklist = Checklist.objects.get(id=checklist_id)

	# Set checklist status to 'Inprogress'
	checklist.status = 'I'
	checklist.save()
		
	# Go through all item and update its status
	for item in checklist.item_set.all():
		# Save selected choice to database
		if str(item.id) in request.POST:
			#return render(request,'checklist/checklist_detail.html', {'checklist': checklist})
			item_choice = request.POST[str(item.id)]
			item.itemStatus = item_choice
			item.save()

	# Always return an HttpResponseRedirect after successfully dealing
	# with POST data. This prevents data from being posted twice if a
	# user hits the Back button.
	return HttpResponseRedirect(reverse('checklist.views.checklist_detail', args=(checklist.id,)))
		
		
# Function to validate items of a checklist, required user to logged in
@login_required(login_url='/checklist/')
def checklist_validate(request, checklist_id):
	#p = get_object_or_404(Poll, pk=poll_id)
	checklist = Checklist.objects.get(id=checklist_id)
	
	# Retrieve all items of this checklist
	items = checklist.item_set.all()
	# Check if there is any item unanswered
	if items is None:
		# Return to the same result page with error message
		error_message = "Checklist is empty!"
		return render(request,'checklist/checklist_detail.html', \
					{'checklist': checklist, 'error_message': error_message})

	# Check if all items of this checklist have status of yes or n/a
	is_validated = True
	for item in items:
		# Set is_validated flag to False if any item is 'Unanswered'
		if item.itemStatus == 'U': is_validated = False
	
	# Return to the same result page with validate message
	if is_validated: validate_message = "Checklist is validated! All items are answered."
	else: validate_message = "Checklist is not validated! At least one item is unanswered."
	return render(request,'checklist/checklist_detail.html', \
					{'checklist': checklist, 'validate_message': validate_message})	


# Function to submit checklist for review, required user to logged in
@login_required(login_url='/checklist/')
def checklist_submit(request, checklist_id):
	#p = get_object_or_404(Poll, pk=poll_id)
	checklist = Checklist.objects.get(id=checklist_id)
	
	# First validate the checklist
	items = checklist.item_set.all()
	# Check if there is any item unanswered
	if items is None:
		# Return to the same result page with error message
		error_message = "Checklist is empty!"
		return render(request,'checklist/checklist_detail.html', \
					{'checklist': checklist, 'error_message': error_message})

	# Check if all items of this checklist have status of yes or n/a
	is_validated = True
	for item in items:
		# Set is_validated flag to False if any item is 'Unanswered'
		if item.itemStatus == 'U': is_validated = False
		
	if is_validated:
		# Set checklist status to 'submited'
		checklist.status = 'S'
		checklist.save()
		
		# Return to the same result page with submit message
		submit_message = "Checklist is submited for review!"
		return render(request,'checklist/checklist_detail.html', \
					{'checklist': checklist, 'submit_message': submit_message})
	else:
		# Return to the same result page with submit message
		submit_message = "Checklist is not validated! Please complete checklist before submition."
		return render(request,'checklist/checklist_detail.html', \
					{'checklist': checklist, 'submit_message': submit_message})
		

