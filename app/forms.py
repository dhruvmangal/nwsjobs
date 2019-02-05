from django import forms

class LoginForm(forms.Form):
    phone = forms.CharField(max_length=200)
    password = forms.CharField(max_length=200)  

    


class SignupForm(forms.Form):
    mobile= forms.CharField(label="mobile", max_length=10)    

class SignupForm2(forms.Form):
    
    name=forms.CharField(label="name", max_length=100) 
    email= forms.CharField(label="email", max_length=100)
    dob= forms.DateField(label="dob" )
    f_name= forms.CharField(label="f_name", max_length=100)
    gender= forms.CharField(label="gender", max_length=10)

class SignupForm4(forms.Form):
    
    job_role= forms.CharField(label="job_role", max_length=100)
    experience= forms.CharField(label="experience", max_length=100)
    current_state= forms.CharField(label="current_state", max_length=100)
    current_city= forms.CharField(label="current_city", max_length=100)
    current_address= forms.CharField(label="current_address", max_length=100)
    permanent_state= forms.CharField(label="permanent_state", max_length=100)
    permanent_city= forms.CharField(label="permanent_city", max_length=100)
    permanent_address= forms.CharField(label="permanent_address", max_length=100)
    job_title= forms.CharField(label="job_title", max_length=100)
    company_address= forms.CharField(label="company_address", max_length=100)
    from_= forms.CharField(label="from", max_length=100)
    to_= forms.CharField(label="to", max_length=100)
    description= forms.CharField(label="description" , max_length=200)

class college_signupForm(forms.Form):
    college_name= forms.CharField(label="college_name", max_length=100)
    mobile_no= forms.CharField(label="mobile_no",max_length=10 )
    email= forms.CharField(label="email", max_length=100)
    state= forms.CharField(label="state", max_length=30)
    city= forms.CharField(label="city", max_length=30)
    password= forms.CharField(widget = forms.PasswordInput())

class college_loginForm(forms.Form):
    mobile_no= forms.CharField(max_length=200)
    password= forms.CharField(max_length=200)    

class event_form(forms.Form):
    event_name = forms.CharField(max_length=200)
    event_venue= forms.CharField(max_length=200)
    event_start_date= forms.CharField(max_length=200)
    event_end_date= forms.CharField(max_length=200)
    event_description= forms.CharField(max_length=200)


class company_signup1(forms.Form):
    mobile=   forms.CharField(max_length=200)  

class regform(forms.Form):
    company_name= forms.CharField(max_length=200)
    contact_person= forms.CharField(max_length=200)
    company_email= forms.CharField(max_length=200)
    company_address= forms.CharField(max_length=200)
    company_password= forms.CharField(max_length=200)

class companysignin(forms.Form):
    mobile_no= forms.CharField(max_length=200)
    password= forms.CharField(max_length=200)