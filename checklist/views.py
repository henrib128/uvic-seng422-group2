# Create your views here.
from django.template import Context, loader
from django.core.context_processors import csrf
#from checklist.models import checklist
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login

def index(request):
	c = {}
	c.update(csrf(request))
	return render_to_response('checklist/index.html',c)
	
	
def home_view(request):
	c = {}
	c.update(csrf(request))
	username = request.POST['username']
	password = request.POST['password']
	user = authenticate(username=username, password=password)
	if user is not None:
		if user.is_active:
			login(request, user)
			# Redirect to a success page.
			return HttpResponse("Login succeeds.",c)
		else:
			# Return a 'disabled account' error message
			return HttpResponse("Unactive account.",c)
	else:
		# Return an 'invalid login' error message.
		return HttpResponse("Invalid login.",c)
		
  
