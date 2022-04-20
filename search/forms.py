
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.postgres.fields.array import ArrayField
from django.forms.fields import CharField
from django.forms.widgets import DateInput, DateTimeInput, TimeInput
from search.models import Professional

class UserForm(UserCreationForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('first_name','last_name', 'username', 'email', 'password1' ,'password2' )


class ProfessionalForm(forms.ModelForm):
    class Meta:
        model = Professional
        fields = ('bio', 'zip_code')


class ProImageForm(forms.ModelForm):
    class Meta:
        model = Professional
        fields = ('headshot', 'work_1', 'work_2', 'work_3')

class ScheduleForm(forms.Form):
    available_schedule = ArrayField(CharField(max_length=7))
    

hair_choices = [
    ('mcut', "Men's Cut"),
    ('wcut', "Women's Cut"),
    ('col', 'Coloring'),
    ('wax', 'Waxing'),
    ('high', 'Highlights'),
    ('con', 'Conditioning'),
    ('bride', 'Bridal'),
    ]

nail_choices = [
    ('reg_man', 'Regular Manicure'),
    ('french_man', 'French Manicure'),
    ('a_fullset', 'Acryllic Full Set'),
    ('reg_ped', 'Regular Pedicure'),
    ('french_ped', 'French Pedicure'),
    ]   

class JobSurvey(forms.Form):
    
    #just make this a normal form
    zip_code = forms.CharField(label='Zip Code', max_length=10)
    #type_of_hair_job = forms.CharField(label='Hair Job', max_length=10)
    
    hair_job = forms.MultipleChoiceField(
        choices=hair_choices,
    )

    
    #widgets = {'date_of_job' : DateInput()} #, 'time_of_job' : TimeInput()