# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import get_object_or_404, render, redirect, HttpResponseRedirect
from django.http import HttpResponse, Http404
from .models import Job, Jobseeker,JobCategory, College, College_event, Plans,Company
from .forms import LoginForm, SignupForm, SignupForm2,SignupForm4, college_signupForm, college_loginForm, event_form, company_signup1, regform, companysignin
import datetime
# Create your views here.
def index(request):
    return render(request, "index.html")

def jobs(request):
    latest_jobs= Job.objects.order_by('-job_date')[:10]
    category= JobCategory.objects.all()
    context= {'latest_jobs':latest_jobs,'category':category}
    if request.method == 'GET':
        if request.GET.get('job_category'):
            job_category= request.GET.get('job_category')
            context= {'latest_jobs':latest_jobs,'category':category,'job_category': job_category}
    else:
        job_category= 'All'   
        context= context['job_category': job_category]
    return render(request, 'jobseeker/jobs.html',context)    

def candidates(request):  
    category= JobCategory.objects.all()
    latest_candidates= Jobseeker.objects.all() [:10]
    context= {'latest_candidates': latest_candidates,'category':category}

    return render(request, 'employer/candidates.html', context)

def login(request):
    return render(request, 'jobseeker/log-mob.html') 

def logout(request):
    try:
      del request.session['phone']
    except:
      pass
    return HttpResponse("<strong>You are logged out.</strong>")

def signup(request):
    return render(request, 'jobseeker/signup.html')                   
       

def category(request):
    category= JobCategory.objects.all()
    context= {'category':category}
    return render(request, 'jobseeker/cat-mob.html', context)    

def jobview(request, job_id):
    try:
        job= Job.objects.get(pk=job_id)
    except Job.DoesNotExist:
        raise Http404("Job does not exists")

    context= {'job': job}       
    return render(request, 'jobseeker/jobview.html', context)


def user_details(request):
    if request.method == 'POST':
        form= SignupForm(request.POST)
        if form.is_valid():
            request.session['mobile']= form.cleaned_data['mobile']
    else:
        form= SignupForm()
    return render(request, 'jobseeker/user_details.html' )

def user_details2(request):
    if request.method == 'POST':
        form= SignupForm2(request.POST)
        if form.is_valid():
            request.session['name'] = form.cleaned_data['name']
            request.session['email']= form.cleaned_data['email']
            
            request.session['fname']= form.cleaned_data['f_name']
            request.session['gender']= form.cleaned_data['gender']
    else:
        form= SignupForm2()
    return render(request, 'jobseeker/user_details2.html' )

def user_details3(request):
    category= JobCategory.objects.all()
    context={'category':category}
    return render(request, 'jobseeker/user_details3.html', context)

def user_details4(request):
    if request.method == 'GET':
        form= SignupForm4(request.GET)
        if form.is_valid():
            a= form.cleaned_data['job_role']
            request.session['job_role']= form.cleaned_data['job_role']
            request.session['experience']= form.cleaned_data['experience']
            request.session['current_state']= form.cleaned_data['current_state']
            request.session['current_city']= form.cleaned_data['current_city']
    else:
        return redirect('../user_details3/')   
    return render(request, 'jobseeker/user_details4.html',{'a':a})    

def loginForm(request):
    if request.method== 'POST':
        form= LoginForm(request.POST)
       
        if form.is_valid():
            phone= form.cleaned_data['phone']
            password= form.cleaned_data['password']

            user= Jobseeker.objects.filter(jobseeker_phone= phone , jobseeker_password= password) 
           
            if not user:
                return redirect('../jobs/')
            else:    
                request.session['phone']= phone  
    return redirect('../jobs/')       


def filter(request):
    return render(request, 'jobseeker/filters.html')     

def location(request):
    return render(request, 'jobseeker/location.html')    

def thanks(request):
    if request.method == 'POST':
        form= SignupForm(request.POST)
        if form.is_valid():
            mobile= form.cleaned_data['mobile']
    else:
        form= SignupForm()
    return render(request, 'jobseeker/thanks.html/',{'mobile':mobile})

def get_mob(request):
    return render(request, 'jobseeker/signup.html')           


def profile(request):
    category= JobCategory.objects.all()
    return render(request, 'jobseeker/profile.html', {'category':category})    


def college_signup(request):
    return render(request, 'college/signup.html')    

def signedup(request):
    if request.method=="POST":
        form= college_signupForm(request.POST)
        if form.is_valid():
            college_name= form.cleaned_data['college_name']
            mobile_no= form.cleaned_data['mobile_no']
            email= form.cleaned_data['email']
            state= form.cleaned_data['state']
            city= form.cleaned_data['city']
            password= form.cleaned_data['password']
            
            college= College.objects.filter(mobile_no= mobile_no)
            if not college:
                p= College(college_name= college_name, mobile_no= mobile_no, email= email, state= state, city= city, password=password )
                p.save()
                request.session['college_phone']= mobile_no
            else:
                return redirect('../college_signup/')    
    else:
        return redirect('../college_signup/')
    return redirect('../college_profile/')    

def college_profile(request):
    mobile_no= request.session['college_phone']
    college= College.objects.filter(mobile_no=mobile_no )
    return render(request, 'college/profile.html',{'college': college})

def college_login(request):
    return render(request, 'college/login.html')    

def college_loggedin(request):
    if request.method=='POST':
        form= college_loginForm(request.POST)
        if form.is_valid():
            mobile_no= form.cleaned_data['mobile_no']
            password=  form.cleaned_data['password'] 

            college= College.objects.filter(mobile_no= mobile_no, password= password) 
            if not college:
                return redirect('../college_login/')
            else:
                 request.session['college_phone']= mobile_no     
    return redirect('../college_profile/')   

def eventForm(request):
    if request.method== "POST":
        form= event_form(request.POST)
        if form.is_valid():
            event_name= form.cleaned_data['event_name']
            event_venue= form.cleaned_data['event_venue']
            event_start_date= form.cleaned_data['event_start_date']
            event_end_date= form.cleaned_data['event_end_date']
            event_description= form.cleaned_data['event_description']

            p= College_event(event_name= event_name, event_venue= event_venue, event_start_date= event_start_date, event_end_date=event_end_date, event_description= event_description)
            p.save()
    return redirect("../college_profile/")        


def company_register(request):
    return render(request, 'employer/signup.html')    

def company_signedup(request):
    if request.method=="POST":
        form= company_signup1(request.POST)
        if form.is_valid():
            request.session["company_phone"]= form.cleaned_data['mobile']
    return redirect('../plans/')   

def plans(request):
    obj= Plans.objects.all()
    return render(request, 'employer/plans.html', {'obj':obj})

def company_signup2(request):
    return render(request, "employer/regform.html")

def regForm(request):
    if request.method=="POST":
        form= regform(request.POST)
        mobile_no= request.session['company_phone']
        if form.is_valid():
            company_name= form.cleaned_data["company_name"]
            contact_person= form.cleaned_data["contact_person"]
            company_email= form.cleaned_data["company_email"]
            company_address= form.cleaned_data["company_address"]
            company_password= form.cleaned_data["company_password"]
        comp= Company.objects.filter(company_phone= mobile_no)
        if not comp:
            p= Company(company_name= company_name, company_phone= mobile_no, contact_person= contact_person, company_email= company_email,comapny_address= company_address,company_password= company_password, company_acc_creation= datetime.datetime.now())   
            p.save()
            request.session["company_phone"]= mobile_no
            return redirect("../company_profile")        
    return redirect("../company_signup2/")


def company_signin(request):
    return render(request, "employer/log-mob.html")

def companylogin(request):
    if request.method=="POST":
        form= companysignin(request.POST)
        if form.is_valid():
            mobile_no= form.cleaned_data["mobile_no"]
            password= form.cleaned_data["password"]
        comp= Company.objects.filter(company_phone= mobile_no, company_password= password)
        if not comp:
            return redirect("../company_signin")
        else:
            request.session["company_phone"]= mobile_no
            return redirect("../company_profile/")       
    return redirect("../company_signin")
