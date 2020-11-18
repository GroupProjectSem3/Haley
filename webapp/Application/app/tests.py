"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".
"""

import django
from django.test import TestCase
from .models import User_profile

# TODO: Configure your database in settings.py and sync before running tests.
userid='katie.patel@gmail.com' 
class ViewTest(TestCase):
    """Tests for the application views."""
    

    if django.VERSION[:2] >= (1, 7):
        # Django 1.7 requires an explicit setup() when running tests in PTVS
        @classmethod
        def setUpClass(cls):
            super(ViewTest, cls).setUpClass()
            django.setup()

    # def test_home(self):
    #     """Tests the home page."""
    #     response = self.client.get('/')
    #     self.assertContains(response, 'Home Page', 1, 200)

    # def test_contact(self):
    #     """Tests the contact page."""
    #     response = self.client.get('/contact')
    #     self.assertContains(response, 'Contact', 3, 200)

    # def test_about(self):
    #     """Tests the about page."""
    #     response = self.client.get('/about')
    #     self.assertContains(response, 'About', 3, 200)

#The login page loads properly
    def test_load_homen(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_load_userHome(self,request):
        userid='katie.patel@gmail.com' 
        #user = User_profile.objects.filter(email=userid)[0]
        request.session['user_id'] = 'katie.patel@gmail.com' 
        response = self.client.get('/userHome')
        self.assertEqual(response.status_code, 200)

    #def test_redirect_to_home(self, request):
            





        
