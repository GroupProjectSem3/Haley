"""
Definition of views.
"""
from django.contrib.auth.models import User,auth
from django.shortcuts import render ,redirect
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from .models import User_profile
from django.contrib import messages

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
    return render(request,'app/changePassword.html')


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
           return render(request,'app/userProfile.html',{'fname':user.get().first_name,'lname':user.get().last_name,'email':user.get().email})
       else:
            messages.info(request,'invalid credentials ')
            return render(request,'app/login1.html')
    else:
         return render(request,'app/login1.html')

def logout(request):
    if(request.session.has_key('user_id')):
        print(request.session['user_id'])
        del request.session['user_id']
    return render(request,'app/login1.html')


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
                    user =   User_profile.objects.create({"email":userid},{set: {"address" : address ,"city":city,"country":country,"zipcode":zipcode,"dob":dob,"gender":gender,"weight":weight,"height":height}})
                    print ('user details') 
                    user.save()
                    print ('user updated')
                    return render(request,'app/userProfile.html')

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


def nextButtonclick(request):
    if request.method == 'POST':
       weight = int(request.POST.get('wt', None))
       print (weight)
       print ('testgingggg')       
       return render(request,'app/diagnosticTool.html')

      #  if(request.session.has_key('filteredList')):
      #   disease_symptoms_list = request.session['filteredList']
      #   disease_symptoms_list  = disease_symptoms_list.filter(symptom_details={"symptom_id":sympId})
      #  else:
      #   disease_symptoms_list = Disease_symptom.objects.filter(symptom_details = {'symptom_id':sympId})

      #    request.session['filteredList'] = disease_symptoms_list
      #    finishedSymp = dict()
      #    for dis_symp in disease_symptoms_list:
      #       if(Diagnosis.symptomWithWeightExists(dis_symp.symptom_details,sympId,weight)):
      #             for symp_det in dis_symp.symptom_details:
      #                #nextSymp[sympId] =  weight
      #                if(symp_det['symptom_id'] !=sympId):
      #                   if(symp_det['symptom_id'] in finishedSymp):
      #                         finishedSymp[symp_det['symptom_id']] += symp_det['weight']
      #                   else:
      #                         finishedSymp[symp_det['symptom_id']] = symp_det['weight']
         
      #    nextSymptom = max(finishedSymp, key=finishedSymp.get)
      #    context = {'id': nextSymptom}
    else:
       print ('Into else part')
       return render(request,'app/diagnosticTool.html',{'testing':'tesing textttt'}) 


def addButton(request):
    if request.method == 'POST':
       symptom = request.POST.get('txtSymptom', None)
       print (symptom)
       print ('add button')
       return render(request,'app/diagnosticTool.html',{'question':'How severe suffering with the symptom - '+symptom})
    else:
       print ('Into else part')
       return render(request,'app/diagnosticTool.html',{'testing':'tesing textttt'}) 