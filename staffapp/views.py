from django.shortcuts import render,redirect
from .forms import StaffForm

from django.conf import settings  #from geeks for geeks
from django.core.mail import send_mail #from geeks for geeks

# Create your views here.

def RegisterVw(request):
    form=StaffForm()
    if request.method=='POST':
        form=StaffForm(request.POST)
        if form.is_valid():
            form.save()
#from geeks for geeks
            subject = 'welcome to Pyspider'
            name=form.cleaned_data['username']
            password=form.cleaned_data['password']
            email=form.cleaned_data['email']
            
            message = f'Hi {name}, thank you for registering in pyspider and password is :-{password}.'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email ]
            send_mail( subject, message, email_from, recipient_list )

            #return redirect('/batch/trainer/')
            return redirect('/staff/login/')
    return render(request,'register.html',{'form':form})