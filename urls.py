from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^polls/$', 'polls.views.index'),
    url(r'^polls/(?P<poll_id>\d+)/$', 'polls.views.detail'),
    url(r'^polls/(?P<poll_id>\d+)/results/$', 'polls.views.results'),
    url(r'^polls/(?P<poll_id>\d+)/vote/$', 'polls.views.vote'),
    #url(r'^checklist/$', 'django.contrib.auth.views.login', {'template_name': 'checklist/index.html'}),
    url(r'^checklist/$', 'checklist.views.index'),
    url(r'^checklist/home_view', 'checklist.views.home_view'),
        
    # url(r'^$', 'seng422gp2.views.home', name='home'),
    # url(r'^seng422gp2/', include('seng422gp2.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
