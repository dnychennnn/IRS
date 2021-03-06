from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'IRS.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^guest/', include('guest.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^ilt_client/', include('ilt_client.urls', namespace="ilt_client")),
)

