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

#Loading feedback page initially  
    def test_for_feeedback(self, request):
        request.session['user_id'] = 'katie.patel@gmail.com'
        response = self.client.get('/feedback')
        self.assertEqual(response.status_code, 200)

#Fetching the diagnosis details in feedback load
    def test_get_diagnosis_feedback(self,request):
        userid = 'katie.patel@gmail.com'
        isAjax = True
        count = 3   # Mocking the data as there are 3 diagnosis results
        if request.is_ajax():
            actionType = 'LOAD'
            if actionType == 'LOAD':
                user_diag = User_diagnosis.objects.filter(user_id=userid,isFeedbackGiven=0)
                if user_diag.__len__() > 0:
                    diag = user_diag.values('id','userResults','create_date')
                    lstDiag = list(diag)
                    for d in lstDiag:
                        d['create_date'] = d['create_date'].strftime("%d %h, %Y %I:%M %p")
                else:
                    lstDiag =[]

                response = self.client.get('/feedback')
                self.assertEqual(count, lstDiag.__len__())
                self.assertJSONEqual(response.content, {'status': 'success'})

#Submitting the feedback details
    def test_submit_feedback(self,request):
        userid = 'katie.patel@gmail.com'
        isAjax = True
        actionType = 'SUBMIT'
        # Mocking the feedabck data
        unq_id = 24
        rating = 4
        ratingText = 'Good'
        count = 2
        response = self.client.get('/feedback')
        if request.is_ajax():
            if actionType == 'SUBMIT':
                User_diagnosis.objects.filter(user_id=userid,id=unq_id).update(isFeedbackGiven=1, feedbackRating=rating,feedbackText=ratingText,modify_date=datetime.today())
                user_diag = User_diagnosis.objects.filter(user_id=userid,isFeedbackGiven=0)
                if user_diag.__len__() > 0:
                    diag = user_diag.values('id','userResults','create_date')
                    lstDiag = list(diag)
                    for d in lstDiag:
                        d['create_date'] = d['create_date'].strftime("%d %h, %Y %I:%M %p")
                    
                else:   
                    lstDiag = []
                
                self.assertEqual(count, lstDiag.__len__())
                self.assertJSONEqual(response.content, {'status': 'success'})

#Fetching when there are no diagnosis details in feedback load
    def test_get_zero_diagnosis_feedback(self,request):
        userid = 'katie.patel@gmail.com'
        isAjax = True
        count = []   # Mocking the data as there are no (i.e., 0) diagnosis results
        if request.is_ajax():
            actionType = 'LOAD'
            if actionType == 'LOAD':
                user_diag = User_diagnosis.objects.filter(user_id=userid,isFeedbackGiven=0)
                if user_diag.__len__() > 0:
                    diag = user_diag.values('id','userResults','create_date')
                    lstDiag = list(diag)
                    for d in lstDiag:
                        d['create_date'] = d['create_date'].strftime("%d %h, %Y %I:%M %p")
                else:
                    lstDiag = []

                response = self.client.get('/feedback')
                self.assertEqual(count, lstDiag)
                self.assertJSONEqual(response.content, {'status': 'success'})                
        
#Loading assessment page with no data
    def test_no_assessments(self, request):
        userid = 'katie.patel@gmail.com'
        assessData = User_diagnosis.objects.filter(user_id=userid).order_by('-create_date')
    if(assessData.__len__() == 0):
        response = self.client.get('/assessmentDetails')
        self.assertEqual(response.status_code, 200) 

#Fetching the assessement details along with feedback also
    def test_get_assessment_details_with_feedback(self,request):
        userid = 'katie.patel@gmail.com'
        # mockup data
        assessData_mk = {"id":1,"user_id":"katie.patel@gmail.com","userResponses":"Itchy Eyes_4|itchy throat_5|Sneezing_3|Itchy mouth_0","userResults":"HAY FEVER","create_date":"2020-12-02T05:19:41.176Z","modify_date":"2020-12-02T05:20:26.740Z","isFeedbackGiven":1,"feedbackRating":4,"feedbackText":"It's Okay"}

        response = self.client.get('/assessmentDetails')

        assessData = User_diagnosis.objects.filter(user_id=userid).order_by('-create_date')
        if(assessData.__len__() > 0):
            assessList = list()
            for assess in assessData:
                assessDic = dict()
                assessDic['id'] = assess.id
                assessDic['dDate'] = assess.create_date.strftime("%d %h, %Y")
                assessDic['dTime'] = assess.create_date.strftime(" %I:%M %p")
                assessDic['diseaseName'] = assess.userResults
                assessDic['isFeedbackGiven'] = assess.isFeedbackGiven
                if assess.isFeedbackGiven == 1:
                    assessDic['feedbackText'] = assess.feedbackText
                    assessDic['feedbackRating'] = assess.feedbackRating
                    assessDic['fDate'] = assess.modify_date.strftime("%d %h, %Y")
                    assessDic['feedbackRatingDesc'] = common.ratingDesc[assess.feedbackRating]
                    assessDic['feedbackRatingImage'] = common.ratingImage[assess.feedbackRating]
                    if assess.create_date.strftime("%d %h, %Y") == assess.modify_date.strftime("%d %h, %Y"):
                        assessDic['fTime'] = assess.modify_date.strftime(" %I:%M %p")
                    else:
                        assessDic['fTime'] = assess.modify_date.strftime(" %d %h, %Y %I:%M %p")

                forSympPresent = list()    
                forSympAbsent = list()
                userResponses = assess.userResponses.split('|')
                for resp in userResponses:
                    Sname = resp.split('_')[0]
                    if resp.split('_')[1] == '0':
                        forSympAbsent.append(Sname)
                    else:
                        forSympPresent.append(Sname) 
                assessDic['symPresent'] = forSympPresent
                assessDic['symAbsent'] = forSympAbsent
                # For description part
                diseaseDesc = Disease.objects.filter(disease_name=assess.userResults)[0].disease_description
                descParts = Diagnosis.splitDescription(diseaseDesc)
                assessDic['disDesc1'] = descParts[0]
                assessDic['disDesc2'] = descParts[1]
                assessList.append(assessDic)
                
        # to check the disease name
        self.assertEqual(assessData_mk.userResults, assessList[0].diseaseName)
        self.assertJSONEqual(response.content, {'status': 'success'}) 

#Fetching the assessement details without any feedback 
    def test_get_assessment_details_with_feedback(self,request):
        userid = 'katie.patel@gmail.com'
        # mockup data
        assessData_mk = {"id":3,"user_id":"katie.patel@gmail.com","userResponses":"Pain during urination_5|Difficulty Urinating_1|Abdominal pain_3|Infection_2","userResults":"BLADDER STONES","create_date":"2020-12-02T16:49:24.118Z","modify_date":"2020-12-02T16:49:24.118Z","isFeedbackGiven":0,"feedbackRating":null,"feedbackText":""}

        response = self.client.get('/assessmentDetails')

        assessData = User_diagnosis.objects.filter(user_id=userid).order_by('-create_date')
        if(assessData.__len__() > 0):
            assessList = list()
            for assess in assessData:
                assessDic = dict()
                assessDic['id'] = assess.id
                assessDic['dDate'] = assess.create_date.strftime("%d %h, %Y")
                assessDic['dTime'] = assess.create_date.strftime(" %I:%M %p")
                assessDic['diseaseName'] = assess.userResults
                assessDic['isFeedbackGiven'] = assess.isFeedbackGiven
                if assess.isFeedbackGiven == 1:
                    assessDic['feedbackText'] = assess.feedbackText
                    assessDic['feedbackRating'] = assess.feedbackRating
                    assessDic['fDate'] = assess.modify_date.strftime("%d %h, %Y")
                    assessDic['feedbackRatingDesc'] = common.ratingDesc[assess.feedbackRating]
                    assessDic['feedbackRatingImage'] = common.ratingImage[assess.feedbackRating]
                    if assess.create_date.strftime("%d %h, %Y") == assess.modify_date.strftime("%d %h, %Y"):
                        assessDic['fTime'] = assess.modify_date.strftime(" %I:%M %p")
                    else:
                        assessDic['fTime'] = assess.modify_date.strftime(" %d %h, %Y %I:%M %p")

                forSympPresent = list()    
                forSympAbsent = list()
                userResponses = assess.userResponses.split('|')
                for resp in userResponses:
                    Sname = resp.split('_')[0]
                    if resp.split('_')[1] == '0':
                        forSympAbsent.append(Sname)
                    else:
                        forSympPresent.append(Sname) 
                assessDic['symPresent'] = forSympPresent
                assessDic['symAbsent'] = forSympAbsent
                # For description part
                diseaseDesc = Disease.objects.filter(disease_name=assess.userResults)[0].disease_description
                descParts = Diagnosis.splitDescription(diseaseDesc)
                assessDic['disDesc1'] = descParts[0]
                assessDic['disDesc2'] = descParts[1]

                assessList.append(assessDic)
        
        # to check the feedback name
        self.assertEqual(assessData_mk.isFeedbackGiven, assessList[0].isFeedbackGiven)
        self.assertJSONEqual(response.content, {'status': 'success'})                 

            