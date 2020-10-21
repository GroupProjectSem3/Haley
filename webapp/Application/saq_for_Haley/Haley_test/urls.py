from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('', 
    url(r'^saq/',include('cms\_saq.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^saq/', include('cms_saq.urls')),
    url(r'^', include('cms.urls')),
)
