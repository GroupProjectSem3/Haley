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
from .models import Disease, Disease_symptom, symptom,Symptom_detail
from .diagnosis import Diagnosis
from django.http import JsonResponse
from django.core.cache import cache
import json
from .symptomEnum import symptomEnum



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
    return render(request,'app/userProfile.html')


def login(request):
    if request.method == 'POST':
       email=request.POST['email']
       pwd =request.POST['password']
        
       #user = auth.authenticate(username=username,password=password)
    #user = User_profile.objects.filter(email=username,password=pwd).exists()
       user = User_profile.objects.filter(email=email,password=pwd)
       if User_profile.objects.filter(email=email,password=pwd).exists():
          return render(request,'app/userProfile.html',{'fname':user.get().first_name,'lname':user.get().last_name,'email':user.get().email})
       else:
            messages.info(request,'invalid credentials ')
            return render(request,'app/login1.html')
    else:
         return render(request,'app/login1.html')

def logout(request):
    return render(request,'app/login1.html')

 



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
                  return render(request,'app/login1.html')
          else:
                messages.info(request,'password not matching...' )
                return redirect( 'register')
          return redirect( 'register')

    else:

         return render(request , 'app/register.html')


def diagnosticTool(request):
    print ('Inside diagnostic tool first page')
    return render(request,'app/diagnosticTool.html',{'testing':'tesing textttt'})   


def addButton(request):
    if request.method == 'POST':
       symptomName = request.POST.get('txtSymptom', None)
       if symptom.objects.filter(symptom_name=symptomName).exists():
          Diagnosis.clearCacheAndSession(request)
          return render(request,'app/diagnosticToolQuestion.html',{'question':symptomName,'symptomId':symptomName})
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
  
   equipment_list = cache.get('disease_symptom_list')
   if not equipment_list:
      disease_symptoms_list = Disease_symptom.objects.filter(symptom_details = {'symptom_id':sympId})
   else:
      disease_symptoms_list = cache.get('disease_symptom_list')

   x = Diagnosis.getNextSymptom(request,disease_symptoms_list,sympId,weight)
   #test = ['S9','S10']
   nxtSymptom = symptomEnum[x[0]].value
   #nxtSymptom = symptom.objects.filter(symptom_id=id)[0].symptom_name

   # For saving response data
#    if(request.session.has_key('response_list')):
#        resp_list = request.session['response_list'] 
#    else:
#        resp_list = list()
#    resp = dict()
#    resp['symptom_id'] = sympId
#    resp['symptom_name'] = symptomName
#    resp['weight'] = weight
#    resp_list.append(resp)
#    request.session['response_list'] = resp_list

   data = {
        'is_taken': True, 
        'nextSymptom': nxtSymptom,
    }
   return JsonResponse(data, safe=False)


def symptom_autocomplete(request):
    if request.is_ajax():
        query = request.GET.get("term", "")
        symptoms = symptom.objects.filter(symptom_name__startswith=query)
        results = []
        for company in symptoms:
            place_json = company.symptom_name
            results.append(place_json)
        data = json.dumps(results)
    mimetype = "application/json"
    return HttpResponse(data, mimetype)





