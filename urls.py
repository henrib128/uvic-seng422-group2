from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	# Examples:
	# Poll application
	url(r'^polls/$', 'polls.views.index'),
	url(r'^polls/(?P<poll_id>\d+)/$', 'polls.views.detail'),
	url(r'^polls/(?P<poll_id>\d+)/results/$', 'polls.views.results'),
	url(r'^polls/(?P<poll_id>\d+)/vote/$', 'polls.views.vote'),

	# Checklist application
	#url(r'^checklist/$', 'django.contrib.auth.views.login', {'template_name': 'checklist/index.html'}),
	url(r'^checklist/$', 'checklist.views.index'),
	url(r'^checklist/login/$', 'checklist.views.login_view'),
	url(r'^checklist/logout/$', 'checklist.views.logout_view'),	
	url(r'^checklist/home/$', 'checklist.views.home'),
	url(r'^checklist/(?P<checklist_id>\d+)/$', 'checklist.views.checklist_detail'),	
	url(r'^checklist/(?P<checklist_id>\d+)/save/$', 'checklist.views.checklist_save'),
	url(r'^checklist/(?P<checklist_id>\d+)/result/$', 'checklist.views.checklist_result'),
	url(r'^checklist/(?P<checklist_id>\d+)/validate/$', 'checklist.views.checklist_validate'),
	url(r'^checklist/(?P<checklist_id>\d+)/submit/$', 'checklist.views.checklist_submit'),
		
	# url(r'^$', 'seng422gp2.views.home', name='home'),
	# url(r'^seng422gp2/', include('seng422gp2.foo.urls')),
	# Uncomment the admin/doc line below to enable admin documentation:
	# url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

	# Uncomment the next line to enable the admin:
	url(r'^admin/', include(admin.site.urls)),
)
