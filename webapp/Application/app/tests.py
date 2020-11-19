"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".
"""

import django
from django.test import TestCase
from .models import User_profile
import json

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

#The login page loads properly
    def test_load_home(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

#Redirecting to user home screen
    def test_load_userHome(self,request):
        userid='katie.patel@gmail.com' 
        #user = User_profile.objects.filter(email=userid)[0]
        request.session['user_id'] = 'katie.patel@gmail.com' 
        response = self.client.get('/userHome')
        self.assertEqual(response.status_code, 200)

#Going to diagnostic tool main page 
    def test_for_diagnosticTool_mainPage(self, request):
        request.session['user_id'] = 'katie.patel@gmail.com'
        response = self.client.get('/diagnosticTool')
        self.assertEqual(response.status_code, 200)

#selecting the valid symptom from the symptom search
    def test_select_symptom_exists(self):
        symptomName = 'Fatigue'
        request.session['user_id'] = 'katie.patel@gmail.com' 
        response = self.client.get('/addButton')
        self.assertEqual(response.status_code, 200)

#selecting an in valid symptom from the symptom search
    def test_select_symptom_not_exists(self):
        symptomName = 'Temperature'
        request.session['user_id'] = 'katie.patel@gmail.com' 
        response = self.client.get('/addButton')
        self.assertEqual(response.status_code, 200)     

#fetching all the related symptom names starts with that letter provided
    def test_symptom_autocomplete(self,request):
        query = 'f'
        response = self.client.get('/symptom_autocomplete')
        result = json.loads(response.content)
        symptom_check = result[0]
        json_string = json.dumps({["Fatigue", "Fever", "Fluid accumulation", "Fidgeting", "Frequent Urination", "Forgetfulness"]})
        self.assertEqual(json_string[0], symptom_check)
        self.assertJSONEqual(
            response.content,
            {'status': 'success'}
        )

#get the details of symptom after selecting the valid symptom
    def test_symptom_getDetails(self,request):
        symptomName = 'Fatigue'
        response = self.client.get('/ajax/getDetails')
        result = json.loads(response.content)
        symptom_value = result.entries_list['symptom']
        json_string = json.dumps([{'desc': 'Fatigue is a term used to describe an overall feeling of tiredness or lack of energy. It isnt the same as simply feeling drowsy or sleepy. When youre fatigued, you have no motivation and no energy', 'symptom': 'Fatigue'}])
        self.assertEqual(json_string[0]['symptom'], symptom_value)
        self.assertJSONEqual(
            response.content,
            {'status': 'success'}
        )

#fetch the next symptom based on the previous response
    def test_on_symptom_nextClick(self):
        weight = 4
        symptomName ='Fatigue'
        sympId = 'S7'
        response = self.client.get('/ajax/symptom_nextClick')
        result = json.loads(response.content)
        next_symptom_value = result['nextSymptom']
        self.assertEqual('Fever', next_symptom_value)
        self.assertEqual(response.status_code, 200)  






        
