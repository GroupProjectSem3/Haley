"""
Definition of urls for python_webapp_django.
"""
from django.contrib.auth import views as auth_views
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
    url(r'^addButton', app.views.addButton, name='addButton'),
    url(r'^ajax/symptom_nextClick/$',
        app.views.symptom_nextClick,
        name='symptom_nextClick'),
    url(r'^api/symptom-autocomplete/',
        app.views.symptom_autocomplete,
        name='symptom-autocomplete'),
    url(r'^update_Profile', app.views.update_Profile, name='update_Profile'),
    url(r'^userProfile', app.views.userProfile, name='userProfile'),
    url(r'^updatePassword', app.views.updatePassword, name='updatePassword'),
    url(r'^changePassword', app.views.changePassword, name='changePassword'),
    url(r'^forget_Password', app.views.forget_Password, name='forget_Password'),
    url(r'^check_email', app.views.check_email, name='check_email'),
    url(r'^reset_Password', app.views.reset_Password, name='reset_Password'),
    url(r'^ajax/getDetails/$', app.views.getDetails, name='getDetails'),
    url(r'^settings', app.views.settings, name='settings'),
    url(r'^GPList', app.views.GPList, name='GPList'),
    url(r'^feedback', app.views.feedback, name='feedback'),
    url(r'^assessmentDetails', app.views.assessmentDetails, name='assessmentDetails'),
    url(r'^ajax/getChartsDetails/$', app.views.getChartsDetails, name='getChartsDetails'),
    url(r'^ajax/getTowns/$', app.views.getTowns, name='getTowns'),
    url(r'^ajax/getGP/$', app.views.getGP, name='getGP'),
    
]