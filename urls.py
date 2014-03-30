from django.conf.urls.defaults import patterns, include, url

from two import views


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'two.views.index', name='home'),
    #url(r'^$', 'two.views.detail', name='detail'),
    #url(r'^(?P<poll_id>\d+)/$', views.detail, name='detail'),

    #url(r'^$', views.IndexView.as_view(), name='index'),
    #url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
    #url(r'^(?P<pk>\d+)/results/$', views.ResultsView.as_view(), name='results'),
    #url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),
    
    
    
    
    #url(r'^(?P<two_id>\d+)/vote/$', views.choice, name='choice'),
    
    # url(r'^one/', include('one.foo.urls')),
    
    #url(r'^polls/$', 'index'),
    #url(r'^polls/(?P<poll_id>\d+)/$', 'detail'),
    #url(r'^polls/(?P<poll_id>\d+)/results/$', 'two.views.results'),
    #url(r'^polls/(?P<poll_id>\d+)/vote/$', 'two.views.vote'),    
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    #url(r'^two/', include('two.urls')),
    #url(r'^$', views.index, name='index'),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)