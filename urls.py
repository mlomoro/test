#from django.conf.urls.defaults import patterns, include, url
from django.conf.urls.defaults import *
from django.views.generic import DetailView, ListView
from polls.models import Poll

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
#	url(r'^polls/$',
#		ListView.as_view(
#			queryset=Poll.objects.order_by('-pub_date')[:5],
#			context_object_name='latest_poll_list',
#			template_name='polls/index.html')),
#	url(r'^polls/(?P<pk>\d+)/$',
#		DetailView.as_view(
#			model=Poll,
#			template_name='polls/detail.html')),
#	url(r'^polls/(?P<pk>\d+)/results/$',
#		DetailView.as_view(
#			model=Poll,
#			template_name='polls/results.html'),
#		name='poll_results'),

    # Examples:
    url(r'^polls/$', 'polls.views.index'),
    url(r'^polls/(?P<poll_id>\d+)/$', 'polls.views.detail'),
    url(r'^polls/(?P<poll_id>\d+)/results/$', 'polls.views.results'),
    url(r'^polls/(?P<poll_id>\d+)/vote/$', 'polls.views.vote'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
