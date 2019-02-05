from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^jobs/', views.jobs, name='index'),
    url(r'^candidates/', views.candidates, name='index'),
    url(r'^login/', views.login, name="login"),
    url(r'^filter/', views.filter, name="filter"),
    url(r'^signup/', views.signup, name="signup"),
    url(r'^category/', views.category, name="category"),
    url(r'^user_details/', views.user_details, name="category"),
    url(r'^user_details2/', views.user_details2, name="category"),
    url(r'^user_details3/', views.user_details3, name="category"),
    url(r'^loginForm/', views.loginForm, name="login"),
    url(r'^location/', views.location, name="login"),
    url(r'^loca/', views.get_mob, name="login"),
    url(r'^(?P<job_id>[0-9]+)/$', views.jobview, name='index'),
    url(r'^jobs/(?P<job_id>[0-9]+)/$', views.jobview, name='index'),
    url(r'^thanks',views.thanks, name="thanks" ),
    url(r'^profile/',views.profile, name="thanks" ),
    url(r'^user_details4/',views.user_details4, name="thanks" ),
    url(r'^college_signup/',views.college_signup, name="thanks" ),
    url(r'^signedup/',views.signedup, name="thanks" ),
    url(r'^college_profile/',views.college_profile, name="thanks" ),
    url(r'^college_login/',views.college_login, name="thanks" ),
    url(r'^college_loggedin/',views.college_loggedin, name="thanks" ),
    url(r'^eventForm/',views.eventForm, name="thanks" ),
    url(r'^company_signup/',views.company_register, name="thanks" ),
    url(r'^company_signedup/',views.company_signedup, name="thanks" ),
    url(r'^plans/',views.plans, name="thanks" ),
    url(r'^company_signup2/',views.company_signup2, name="thanks" ),
    url(r'^regForm/',views.regForm, name="thanks" ),
    url(r'^company_signin/',views.company_signin, name="thanks" ),
    url(r'^company_login/',views.companylogin, name="thanks" ),
]