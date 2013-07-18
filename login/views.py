# Create your views here.
from django.template import Context, loader
from django.core.context_processors import csrf
#from checklist.models import checklist
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.contrib.auth import logout

def index(request):
	c = {}
	c.update(csrf(request))
	
	if request.user.is_authenticated():
		return HttpResponseRedirect('/login/home')
	
	if 'username' not in request.POST or 'password' not in request.POST:
		return render_to_response('login/index.html',c)
	
	username = request.POST['username']
	password = request.POST['password']
			
	user = authenticate(username=username, password=password)
	
	if user is not None:
		if user.is_active:
			login(request, user)
			return HttpResponseRedirect('/login/home')
			
		else:
			c = Context({
				'login_error': "Unactive account",
			})
			return HttpResponse('login/index.html', c)
			
	else:
		c = Context({
			'login_error': "Invalid login",
		})
		return HttpResponse('login/index.html', c)

def home(request):
	c = {}
	c.update(csrf(request))
	
	if not request.user.is_authenticated():
		return render_to_response('login/index.html',c)
		
	return render_to_response('login/home.html',c)
	
def logout_view(request):
	logout(request)
	return HttpResponseRedirect('/login')
	
def assigned_checklists_view(request):
	if not request.user.groups.get(name='surveyors'):
		return HttpResponse("You don't have permission to see this page.")
	
	return HttpResponse("Assigned Checklists")
	
