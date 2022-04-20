from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from search.forms import UserForm
from search.forms import ProfessionalForm, ProImageForm, JobSurvey, ScheduleForm
from search.models import Professional
from django.http import HttpResponse
import json
from django.core import serializers
from django.http import JsonResponse
from django.forms.models import model_to_dict


def home(request):
    return render(request, "search/general_home.html",)

def customer_survey(request):
    if request.method == 'POST':
        customer_form = JobSurvey(request.POST)
        if customer_form.is_valid():
            request.session['zip_code'] = customer_form.cleaned_data.get('zip_code')
            request.session['hair_job'] = customer_form.cleaned_data.get('hair_job')
            return redirect(hair_pros)
        else:
            return render(request, 'search/customer_survey.html', {'customer_form': customer_form})
    else:
        customer_form = JobSurvey()
    return render(request, 'search/customer_survey.html', {'customer_form': customer_form})


def hair_pros(request):
    professionals = Professional.objects.all()
    queried_pros = []
    for pro in professionals:
        for skill in pro.skills:
            if skill in request.session['hair_job']:
                queried_pros.append(pro)

    return render(request, "search/hair_pros.html", {'pros' : queried_pros})


def signin(request):
    if request.user.is_authenticated:
        return redirect(pro_home)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(pro_home)
        else:
            form = AuthenticationForm(request.POST)
            return render(request, 'search/signin.html', {'form': form})
    else:
        form = AuthenticationForm()
        return render(request, 'search/signin.html', {'form': form})

def signup(request):
    if request.user.is_authenticated:
        return redirect(pro_home)
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        professional_form = ProfessionalForm(request.POST)
        if user_form.is_valid() and professional_form.is_valid():
            user = user_form.save()
            user.professional.bio = professional_form.cleaned_data.get('bio')
            user.professional.zip_code = professional_form.cleaned_data.get('zip_code')
            login(request, user)
            return redirect(pro_home)
        else:
            return render(request, 'search/signup.html', {'user_form': user_form, 'professional_form': professional_form})
    else:
        user_form = UserForm()
        professional_form = ProfessionalForm()
        return render(request, 'search/signup.html', {'user_form': user_form, 'professional_form':professional_form})

def signout(request):
    logout(request)
    return render(request, 'search/signout.html')

def pro_home(request):
    professional = request.user.professional
    if request.method == 'POST':
        if 'headshot' in request.POST:
            form = ProImageForm(request.POST, request.FILES, instance=professional)
            if form.is_valid():
                form.save()
                imageform = ProImageForm() #I think this is correct
                scheduleform = ScheduleForm()
                return render(request, "search/pro_home.html", {'imageForm' : imageform, 'scheduleForm' : scheduleform, 'pro' : professional})

        if 'schedule' in request.POST:
            form = ScheduleForm(request.POST)
            if form.is_valid():
                form.save()
    else:
        imageform = ProImageForm()
        scheduleform = ScheduleForm()
        return render(request, "search/pro_home.html", {'imageForm' : imageform, 'scheduleForm' : scheduleform, 'pro' : professional})
