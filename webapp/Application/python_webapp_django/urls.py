
"""
Definition of urls for python_webapp_django.
"""

from datetime import datetime
from django.conf.urls import url
import django.contrib.auth.views

import app.forms
import app.views

# Uncomment the next lines to enable the admin:
# from django.conf.urls import include
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    # Examples:
    url(r'^$', app.views.home, name='home'),
    url(r'^userHome', app.views.userHome, name='userHome'),
    url(r'^register', app.views.register, name='register'),
    url(r'^login', app.views.login, name='login'),
    url(r'^logout', app.views.logout, name='logout'),
    url(r'^diagnosticTool', app.views.diagnosticTool, name='diagnosticTool'),
    # url(r'^nextButtonclick', app.views.nextButtonclick, name='nextButtonclick'),
    url(r'^addButton', app.views.addButton, name='addButton'),
    # url(r'^update_Profile', app.views.update_Profile, name='update_Profile'),
    # url(r'^newDiagnosticPageClick/(?:(?P<question>.+)/)?$', app.views.newDiagnosticPageClick, name='newDiagnosticPageClick'),
    url(r'^ajax/symptom_nextClick/$', app.views.symptom_nextClick, name='symptom_nextClick'),
    url(r'^api/symptom-autocomplete/', app.views.symptom_autocomplete, name='symptom-autocomplete'),
    url(r'^update_Profile', app.views.update_Profile, name='update_Profile'),
    url(r'^userProfile', app.views.userProfile, name='userProfile'),
    url(r'^updatePassword', app.views.updatePassword, name='updatePassword'),
    url(r'^changePassword', app.views.changePassword, name='changePassword'),
    url(r'^forgotPassword', app.views.forgotPassword, name='forgotPassword'),
    # url(r'^ajax/validate_email/$', app.views.validate_email, name='validate_email'),


    # url(r'^contact$', app.views.contact, name='contact'),
    # url(r'^about', app.views.about, name='about'),
    # url(r'^login/$',
    #     django.contrib.auth.views.login,
    #     {
    #         'template_name': 'app/login.html',
    #         'authentication_form':     #app.forms.BootstrapAuthenticationForm,
    #         'extra_context':
    #         {
    #             'title': 'Log in',
    #             'year': datetime.now().year,
    #         }
    #     },
    #     name='login'),
    # url(r'^logout$',
    #     django.contrib.auth.views.logout,
    #     {
    #         'next_page': '/',
    #     },
    #     name='logout'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
]