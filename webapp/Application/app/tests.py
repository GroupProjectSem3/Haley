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



#Authenticating user while login
    def test_login(self, request):
        emailid ='katie.patel@gmail.com'
        pwd='katie123'

        if User_profile.objects.filter(email=emailid, password=pwd).exists():
            #request.session['user_id'] = emailid
            response = self.client.get('/login')
            self.assertEqual(response.status_code, 200)
        
        else:
             response = self.client.get('/')
             self.assertEqual(response.status_code, 200)

 #registering the new user through register
    def test_register(self):
         fname='Katie'
         lname='Patel'
         emailid ='katie.patel@gmail.com'
         pwd='katie123'
         cpwd='katie123'


         if pwd == cpwd:
            if User_profile.objects.filter(email=emailid).exists():
                print('Email Taken')
                response = self.client.get('/register')
                self.assertEqual(response.status_code, 200)


            else:
                user = User_profile.objects.create(
                    first_name=fname,
                    last_name=lname,
                    email=emailId,
                    password=pwd,
                    confirm_password=cpwd)
                user.save()
                response = self.client.get('/login')
                self.assertEqual(response.status_code, 200)
         else:
            print('Passwords not matched...')
            response = self.client.get('/register')
            self.assertEqual(response.status_code, 200)

 #updating the existing users profile
   def test_update_Profile(self):
        address = 'Lucan'
        country = 'Ireland'
        city = 'Dublin'
        zipcode = '1234'
        dob = '01/02/2000'
        gender = 'female'
        weight = '70.00'
        height = '125.00'

        userid='Katie.patel@gmail.com'

        if User_profile.objects.filter(email=userid).exists():
                User_profile.objects.filter(email=userid).update(
                    address=address,
                    city=city,
                    country=country,
                    zipcode=zipcode,
                    dob=dob,
                    gender=gender,
                    weight=weight,
                    height=height)

                response = self.client.get('/update_Profile')
                self.assertEqual(response.status_code, 200)

    
        
 #user logout from system
   def test_logout(self):
        response = self.client.get('/logout')
        self.assertEqual(response.status_code, 200)
    
#redirecting to user profile 
   def test_load_userProfile(self,request):
        response = self.client.get('/userProfile')
        self.assertEqual(response.status_code, 200)

#user changing the password
   def test_updatePassword(self):
        npass = 'katie111'
        cpass = 'katie111'

        userid='Katie.patel@gmail.com'

         if (npass == cpass):
                
                User_profile.objects.filter(email=userid).update(password=cpass, confirm_password=cpass)
                response = self.client.get('/updatePassword')
                self.assertEqual(response.status_code, 200)

         else:
                response = self.client.get('/updatePassword')
                self.assertEqual(response.status_code, 200)

   #redirecting to update password page
   def test_changePassword(self):
        response = self.client.get('/changePassword')
        self.assertEqual(response.status_code, 200)

 #redirecting to Find Nearby GP's page
   def test_GPList(self):
        response = self.client.get('/GPList')
        self.assertEqual(response.status_code, 200)






        
