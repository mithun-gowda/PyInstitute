from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import TrainerForm,SubjectForm,BatchForm
from .models import Trainer,Subject,BatchDB
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

#firts page not found
def Mainvw(request):
    return render(request,'main.html')

@login_required(login_url='/staff/login/')
def SubjectVW(request):
    form=SubjectForm()
    if request.method =='POST':
        form=SubjectForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request,'subject.html',{'form':form})

@login_required(login_url='/staff/login/')
def TrainerVW(request):
    form=TrainerForm()
    if request.method =='POST' and request.FILES:
        print(request.FILES)
        form=TrainerForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('trainer profile is created')

    return render(request,'trainer.html',{'form':form})


@login_required(login_url='/staff/login/')
def TranierDisplay(request):
    data=Trainer.objects.all()
    
    return render(request,'profiles.html',{'data':data})

@login_required(login_url='/staff/login/')
def TrainerUP(request,pk):
    data = Trainer.objects.get(tid=pk)
    form=TrainerForm(instance=data)
    if request.method =='POST' and request.FILES:
        print(request.FILES)
        form=TrainerForm(request.POST,request.FILES,instance=data)
        if form.is_valid():
            form.save()
            return redirect('/batch/profile/')
    return render(request,'trainerupdate.html',{'form':form,'data':data})

@login_required(login_url='/staff/login/')
def BatchVW(request):
    form=BatchForm()
    if request.method =='POST':
        form=BatchForm(request.POST)
        if form.is_valid():
            form.save()
            a=form.cleaned_data['bid']
            messages.success(request,f"{a} batch is successfully created")
            return redirect('/batch/bdisplay/')
    return render(request,'batch.html',{'form':form})


@login_required(login_url='/staff/login/')
def BatchDisplay(request):
    data=BatchDB.objects.all()
    return render(request,'batchdis.html',{'data':data})

@login_required(login_url='/staff/login/')
def Home(request):
    return render(request,'home.html')