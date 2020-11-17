"""
Definition of views.
"""
from django.contrib.auth.models import User,auth
from django.shortcuts import render ,redirect
from django.http import HttpRequest, HttpResponse
from django.template import RequestContext
from datetime import datetime
from .models import User_profile
from django.contrib import messages
from .models import Disease, Disease_symptom, symptom,Symptom_detail,User_diagnosis
from .diagnosis import Diagnosis
from django.http import JsonResponse
from django.core.cache import cache
import json
from .symptomEnum import symptomEnum
from django.db.models import Q
from django.template.loader import render_to_string
from .diagnosisPrediction import DiagnosisPrediction
from django.contrib.auth.decorators import login_required



# def home(request):
#     """Renders the home page."""
#     assert isinstance(request, HttpRequest)
#     return render(
#         request,
#         'app/userHome.html',
#         {
#             'title':'Home Page',
#             'year':datetime.now().year,
#         }
#     )

# def contact(request):
#     """Renders the contact page."""
#     assert isinstance(request, HttpRequest)
#     return render(
#         request,
#         'app/contact.html',
#         {
#             'title':'Contact',
#             'message':'Your contact page.',
#             'year':datetime.now().year,
#         }
#     )

# def about(request):
#     """Renders the about page."""
#     assert isinstance(request, HttpRequest)
#     return render(
#         request,
#         'app/about.html',
#         {
#             'title':'About',
#             'message':'Your application description page.',
#             'year':datetime.now().year,
#         }
#     )

def home(request):
    #return HttpResponse("Hello. This is the page in app")
    return render(request,'app/signIn.html')

# @login_required(login_url='/login')
def userHome(request):
    if request.method == 'GET':
        print('inside changePassword method') 
        print(request.session['user_id'])
        userid=request.session['user_id']
        print(userid)

        #user = User_profile.objects.get(email=userid).first_name
        # request.session['user_id'] = user.get().email
        # print(request.session['user_id'])
       
        user =User_profile.objects.filter(email = userid)[0]
        print(user.dob)
        print(user)
        print('inside if') 
        return render(request,'app/home.html',{'fname':user.first_name,'lname':user.last_name})#'email':user.email,'address':user.address,'dob':user.dob,'country':user.country,'city':user.city,'zipcode':user.zipcode,'gender':user.gender,'weight':user.weight,'height':user.height})
    else:
           return render(request,'app/userProfile.html')

def login(request):
    if request.method == 'POST':
       email=request.POST['email']
       pwd =request.POST['password']
        
       #user = auth.authenticate(username=username,password=password)
    #user = User_profile.objects.filter(email=username,password=pwd).exists()
       user = User_profile.objects.filter(email=email,password=pwd)
       if User_profile.objects.filter(email=email,password=pwd).exists():
           request.session['user_id'] = user.get().email
           print(request.session['user_id'])
           return render(request,'app/home.html',{'fname':user.get().first_name,'lname':user.get().last_name}) #'email':user.get().email,'address':user.get().address,'dob':user.get().dob,'country':user.get().country,'city':user.get().city,'zipcode':user.get().zipcode,'gender':user.get().gender,'weight':user.get().weight,'height':user.get().height})
       else:
            messages.info(request,'invalid credentials ')
            return render(request,'app/signIn.html')
    else:
         return render(request,'app/signIn.html')

def logout(request):
    if(request.session.has_key('user_id')):
        print(request.session['user_id'])
        del request.session['user_id']
    return render(request,'app/signIn.html')


def update_Profile(request):
   print('inside update')
   if request.method == 'POST':
           address =request.POST['address']
           country=request.POST['country']
           city=request.POST['city']
           zipcode =request.POST['zipcode']
           dob=request.POST['dob']
           gender =request.POST['gender']
           weight =request.POST['weight']
           height =request.POST['height']

           print(request.session['user_id'])
           if(request.session.has_key('user_id')):
                    userid = request.session['user_id']

                    if User_profile.objects.filter(email = userid).exists():
                      User_profile.objects.filter(email = userid).update(address=address,city=city,country=country,zipcode=zipcode,dob=dob,gender=gender,weight=weight,height=height)
                      print ('user details') 
                    # user.save()
                      user =User_profile.objects.filter(email = userid)[0]
                      print ('user updated')
                      return render(request,'app/userProfile.html',{'fname':user.first_name,'lname':user.last_name,'email':user.email,'address':user.address,'dob':user.dob,'country':user.country,'city':user.city,'zipcode':user.zipcode,'gender':user.gender,'weight':user.weight,'height':user.height})
                    else:
                        print ('login first')
           else:
                 return render(request,'app/userProfile.html')
          
 
   else: 
       return render(request,'app/userProfile.html')
 

def register(request):
    if  request.method == 'POST':
          fName =request.POST['first_name']
          lName =request.POST['last_name']
          emailId =request.POST['email']
          pwd =request.POST['password']
          confirmPassword =request.POST['confirmPassword']
       
          if pwd==confirmPassword:
             if User_profile.objects.filter(email=emailId).exists(): 
                  messages.info(request ,'Email Taken')
                  return redirect( 'register')
             else:
                  user = User_profile.objects.create(first_name=fName,last_name=lName,email=emailId,password=pwd,confirm_password=confirmPassword)
                  user.save()
                  print ('user created')
                  return render(request,'app/signIn.html')
          else:
                messages.info(request,'password not matching...' )
                return redirect( 'register')
          return redirect( 'register')

    else:

         return render(request , 'app/signUp.html')

# @login_required
def diagnosticTool(request):
    print ('Inside diagnostic tool first page')
    #return render(request,'app/diagnosticTool.html',{'testing':'tesing textttt'})   
    userid = request.session['user_id']
    user =User_profile.objects.filter(email = userid)[0]
    return render(request,'app/diagnosticTool.html',{'fname':user.first_name,'lname':user.last_name})#,##{'fname':user.first_name,'lname':user.last_name})   



def addButton(request):
    if request.method == 'POST':
       symptomName = request.POST.get('txtSymptom', None)
       symptomName = request.POST.get('btnSelect')
       if symptom.objects.filter(symptom_name=symptomName).exists():
          Diagnosis.clearCacheAndSession(request)
          userid = request.session['user_id']
          user =User_profile.objects.filter(email = userid)[0]
          sympDesc = symptom.objects.filter(symptom_name=symptomName)[0].symptom_description
          return render(request,'app/diagnosticToolQuestion.html',{'question':symptomName,'symptomId':symptomName,'symptomDescription':sympDesc,'fname':user.first_name,'lname':user.last_name,'test':'SHOW'})
       else:
          messages.info(request,'Please Select from list')
          return render(request,'app/diagnosticTool.html',{'testing':'tesing textttt'})   
      #  symptom = request.POST.get('txtSymptom', None)
      #  print (symptom)
      #  print ('add button')
      #  Diagnosis.clearCacheAndSession(request)
      #  return render(request,'app/diagnosticToolQuestion.html',{'question':symptomName,'symptomId':symptomName})


def symptom_nextClick(request):
   weight = int(request.GET.get('wt', None))
   symptomName = request.GET.get('symp', None)
   #sympId = 'S7'
   sympId = symptom.objects.filter(symptom_name=symptomName)[0].symptom_id
   
   #
#    tempList = Disease_symptom.objects.all()
#    cache.set('disease_symptom_list',tempList)


   equipment_list = cache.get('disease_symptom_list')
   if not equipment_list:
      disease_symptoms_list = Disease_symptom.objects.filter(symptom_details = {'symptom_id':sympId})
   else:
      disease_symptoms_list = cache.get('disease_symptom_list')

   x = Diagnosis.getNextSymptom(request,disease_symptoms_list,sympId,weight)
   #nxtSymptom = symptomEnum[x].value

   #For saving response data
   if(request.session.has_key('response_list')):
       resp_list = request.session['response_list'] 
   else:
       resp_list = list()
   resp = symptomName+'_'+str(weight)
   resp_list.append(resp)
   request.session['response_list'] = resp_list

   if x != "SUBMITNOW":
       nxtSymptom = symptomEnum[x].value
       sympDesc = symptom.objects.filter(symptom_name=nxtSymptom)[0].symptom_description
       data = {
           'is_taken': True, 
           'nextSymptom': nxtSymptom,
           'question':nxtSymptom,'symptomDescription':sympDesc,
        }
   elif x == "SUBMITNOW":
       userResp = request.session['response_list']
       response_list = list()
       for resp in userResp:
           if resp.split('_')[1] !='0':
               response_list.append(resp.split('_')[0])
       # To get the predictions        
       userResu = DiagnosisPrediction.predict(response_list)
       #user_results = '|'.join(userResu)
       user_results = userResu[0]
       #user_results = 'DIABTIES'
       user_responses = '|'.join(userResp)
       userid=request.session['user_id']
       user_diag = User_diagnosis.objects.create(user_id=userid,userResponses=user_responses,userResults=user_results,create_date=datetime.today(),modify_date=datetime.today(),isFeedbackGiven=0) 
       user_diag.save()
       # For Diseases with its details
       disease_details = Disease.objects.filter(disease_name=user_results)[0]
       forDiseases = user_results
       forDesc = disease_details.disease_description
       forCauses = disease_details.disease_causes
       forLink = disease_details.link
       # For symptoms with its details
       forSympPresent = list()    
       forSympAbsent = list()
       for resp in userResp:
           Sname = resp.split('_')[0]
           if resp.split('_')[1] == '0':
               forSympAbsent.append(Sname)
           else:
               forSympPresent.append(Sname)    
       data = {
           'is_taken': False,
           'forDiseases': forDiseases, 'forDesc': forDesc, 'forCauses': forCauses,'forLink': forLink,
           'forSympPresent': forSympPresent, 'forSympAbsent' : forSympAbsent,
       }

   return JsonResponse(data, safe=False)


def symptom_autocomplete(request):
    if request.is_ajax():
        query = request.GET.get("term", "")
        #symptoms = symptom.objects.filter(symptom_name__startswidth=query)
        symptoms = symptom.objects.filter(symptom_name__istartswith=query)
        #x = symptom.objects.filter(Q(symptom_name__icontains='fever') | Q(symptom_id__icontains='S3'))
        results = []
        for company in symptoms:
            place_json = company.symptom_name
            results.append(place_json)
        data = json.dumps(results)
    mimetype = "application/json"
    return HttpResponse(data, mimetype)


def getDetails(request):
   symptomName = request.GET.get('symp', None)
   nxtSymptom = list()   
   #symptoms = symptom.objects.filter(Q(symptom_name__icontains=symptomName) | Q(symptom_description__icontains=symptomName))
   symptoms = symptom.objects.filter(Q(symptom_name__icontains=symptomName))
   for symp in symptoms:
       sympDict = dict()
       sympDict['symptom'] = symp.symptom_name
       sympDict['desc'] = symp.symptom_description
       nxtSymptom.append(sympDict)

#    nxtSymptom = [
#        {
#            "symptom":"Fever",
#            "desc" :" Some description that tells about the symptom"
#        },
#        {
#             "symptom":"Fever 1",
#             "desc" :" Some description that tells about the symptom"
#        },
#        {
#             "symptom":"Fever 2",
#             "desc" :" Some description that tells about the symptom"
#        }
#        ]

   data = {
        'is_taken': True, 
        'entries_list': nxtSymptom,
    }
   return JsonResponse(data, safe=False)
   #return render(request,'app/diagnosticTool.html',{'entries_list':nxtSymptom})   



# def addButton(request):
#     if request.method == 'POST':
#        symptom = request.POST.get('txtSymptom', None)
#        print (symptom)
#        print ('add button')
#        return render(request,'app/diagnosticTool.html',{'question':'How do you rate the severity of this symptom - '+symptom})
#     else:
#        print ('Into else part')
#        return render(request,'app/diagnosticTool.html',{'testing':'tesing textttt'}) 

def userProfile(request):
    #   if  request.method == 'GET':
    #       fName =request.GET['first_name']
    #       lName =request.GET['last_name']
    #       emailId =request.GET['email']
    #       pwd =request.GET['password']
    #       confirmPassword =request.GET['confirmPassword']
    #       address =request.GET['address']
    #       country=request.GET['country']
    #       city=request.GET['city']
    #       zipcode =request.GET['zipcode']
    #       dob=request.GET['dob']
    #       gender =request.GET['gender']
    #       weight =request.GET['weight']
    #       height =request.GET['height']

    #       user = User_profile.objects.filter(email=emailId,password=pwd)
    #       if User_profile.objects.filter(email=emailId,password=pwd).exists():
            
          
    #          return render(request,'app/userProfile.html',{'fname':user.get().fName,'lname':user.get().lName,'email':user.get().emailId,'address':user.get().address,'country':user.get().country,'city':user.get().city,'zipcode':user.get().zipcode,'gender':user.get().gender,'weight':user.get().weight,'height':user.get().height})
    #       else:
    #         messages.info(request,'invalid credentials ')
    #   return render(request,'app/login1.html')
    if request.method == 'GET':
        print('inside user Profile method') 
        print(request.session['user_id'])
        userid=request.session['user_id']
        print(userid)

        #user = User_profile.objects.get(email=userid).first_name
        # request.session['user_id'] = user.get().email
        # print(request.session['user_id'])
       
        user =User_profile.objects.filter(email = userid)[0]
        print(user.dob)
        print(user)
        print('inside if') 
        return render(request,'app/userProfile.html',{'fname':user.first_name,'lname':user.last_name,'email':user.email,'address':user.address,'dob':user.dob,'country':user.country,'city':user.city,'zipcode':user.zipcode,'gender':user.gender,'weight':user.weight,'height':user.height})
    else:
           return render(request,'app/userHome.html')
    

def updatePassword(request):
   if request.method == 'POST':
           npass =request.POST['pass1']
           cpass=request.POST['pass2']
           userid = request.session['user_id']
           user =User_profile.objects.filter(email = userid)[0]
           print(request.session['user_id'])
           if(request.session.has_key('user_id')):
                   
                    if (npass==cpass):
                        print('password change')
                        User_profile.objects.filter(email = userid).update(password=cpass,confirm_password=cpass)
                   
                    # user.save()
                        print ('pass updated')
                        return render(request,'app/changePassword.html',{'fname':user.first_name,'lname':user.last_name})

                    else:
                        print ('password not matches')
                        return render(request,'app/changePassword.html')
           else:
                 return render(request,'app/changePassword.html',{'fname':user.first_name,'lname':user.last_name})
          
 
   else: 
         return render(request,'app/userProfile.html')



def changePassword(request):
    if request.method == 'GET':
        print('inside changePassword method') 
        print(request.session['user_id'])
        userid=request.session['user_id']
        print(userid)

        #user = User_profile.objects.get(email=userid).first_name
        # request.session['user_id'] = user.get().email
        # print(request.session['user_id'])
       
        user =User_profile.objects.filter(email = userid)[0]
        print(user.dob)
        print(user)
        print('inside if') 
        return render(request,'app/changePassword.html',{'fname':user.first_name,'lname':user.last_name})#'email':user.email,'address':user.address,'dob':user.dob,'country':user.country,'city':user.city,'zipcode':user.zipcode,'gender':user.gender,'weight':user.weight,'height':user.height})
    else:
           return render(request,'app/userProfile.html')

def forgotPassword(request):
    return render(request,'app/forgotPassword.html') 

# def validate_email(request):
#    email = request.GET.get('email', None)
#    data = {
#         'is_taken': User_profile.objects.filter(email__iexact=email).exists(), 
        
#     }
#    return JsonResponse(data)
def predictions(request):
    return render(request,'app/predictions.html') 


def GPList(request):
    userid = request.session['user_id']
    user =User_profile.objects.filter(email = userid)[0]
    return render(request,'app/GPList.html',{'fname':user.first_name,'lname':user.last_name})   

     
def feedback(request):
    userid = request.session['user_id']
    user = User_profile.objects.filter(email = userid)[0]
    if request.is_ajax():
        actionType = request.GET.get('type', None)
        if actionType == 'LOAD':
            user_diag = User_diagnosis.objects.filter(user_id=userid,isFeedbackGiven=0)
            #user_diag = User_diagnosis.objects.filter(user_id=userid)
            if user_diag.__len__() > 0:
                diag = user_diag.values('id','userResults')
                data = {
                    'is_taken': True,'diag':list(diag),
                    }
            else:
                data = {'is_taken': True,'diag':[],}
            return JsonResponse(data, safe=False)
        elif actionType == 'SUBMIT':
            unq_id = request.GET.get('unique_id', None)
            rating = request.GET.get('rating', None)
            ratingText = request.GET.get('ratingText', None)
            #User_diagnosis.objects.filter(user_id=userid,id=unq_id).update(isFeedbackGiven=1, feedbackRating=5,feedbackText='')
            User_diagnosis.objects.filter(user_id=userid,id=unq_id).update(isFeedbackGiven=1, feedbackRating=rating,feedbackText=ratingText)
            user_diag = User_diagnosis.objects.filter(user_id=userid)
            if user_diag.__len__() > 0:
                diag = user_diag.values('id','userResults')
                data = {
                    'is_taken': True,'diag':list(diag),
                    }
            else:   
                data = {'is_taken': True,'diag':[],}
            return JsonResponse(data, safe=False)
    elif request.method == 'GET' :
        return render(request,'app/feedback.html',{'fname':user.first_name,'lname':user.last_name})
       

def assessmentDetails(request):
    return render(request,'app/userProfile.html')

# def assessmentDetails(request):
#     userid = request.session['user_id']
#     assessData = User_diagnosis.objects.filter(user_id=userid)
#     if(assessData.__len__() > 0):
#         assessList = list()
#         for assess in assessData:
#             assessDic = dict()
#             assessDic['date'] = assess.create_date
#             assessDic['time'] = assess.create_date
#             assessDic['userResult'] = assess.userResults
#             #assessDic['feedbackText'] = assess.feedbackText
#             #assessDic['feedbackRating'] = assess.feedbackRating

#             forSympPresent = list()    
#             forSympAbsent = list()
#             userResponses = assess.userResponses.split('|')
#             for resp in userResponses:
#                 Sname = resp.split('_')[0]
#                 if resp.split('_')[1] == '0':
#                     forSympAbsent.append(Sname)
#                 else:
#                     forSympPresent.append(Sname) 
#             assessDic['symPresent'] = forSympPresent
#             assessDic['symAbsent'] = forSympAbsent

#             assessList.append(assessDic)

#     return render(request,'app/userProfile.html')

