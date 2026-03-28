from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from django.contrib import messages

from .models import Semester,Subject,Unit,Video,PDF
from .forms import RegisterForm


def home(request):

    semesters=Semester.objects.all()

    return render(request,'home.html',{'semesters':semesters})


def register_view(request):

    if request.method=="POST":

        form=RegisterForm(request.POST)

        if form.is_valid():

            username=form.cleaned_data['username']
            email=form.cleaned_data['email']
            password=form.cleaned_data['password']

            User.objects.create_user(
                username=username,
                email=email,
                password=password
            )

            return redirect('login')

    else:

        form=RegisterForm()

    return render(request,'register.html',{'form':form})


def login_view(request):

    if request.method=="POST":

        username=request.POST.get("username")
        password=request.POST.get("password")

        user=authenticate(request,username=username,password=password)

        if user:

            login(request,user)

            return redirect('home')

        else:

            messages.error(request,"Invalid login")

    return render(request,'login.html')


def logout_view(request):

    logout(request)

    return redirect('login')


def subjects(request,semester_id):

    subjects=Subject.objects.filter(semester_id=semester_id)

    return render(request,'subjects.html',{'subjects':subjects})


def units(request,subject_id):

    units=Unit.objects.filter(subject_id=subject_id)
    pdfs=PDF.objects.filter(subject_id=subject_id)

    return render(request,'units.html',{'units':units,'pdfs':pdfs})


def videos(request,unit_id):

    videos=Video.objects.filter(unit_id=unit_id)

    return render(request,'videos.html',{'videos':videos})


def about(request):

    return render(request,'about.html')