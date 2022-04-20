from django.db import models
from multiselectfield import MultiSelectField
from django.contrib.postgres.fields import ArrayField
from django.db.models.fields.files import ImageField
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.forms.widgets import DateInput, DateTimeInput



class Professional(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    zip_code = models.CharField(max_length=30)
    distance = models.CharField(max_length=30, default="Near")
    headshot = models.ImageField(upload_to='images/', default='default.jpeg')
    work_1 = models.ImageField(upload_to='images/', default='default.jpeg')
    work_2 = models.ImageField(upload_to='images/', default='default.jpeg')
    work_3 = models.ImageField(upload_to='images/', default='default.jpeg')
    rating = models.CharField(max_length=3, default='N/A')
    available_schedule = ArrayField(models.CharField(max_length=7, blank=True), default=list)
    
    hair_skills = (
        ('mcut', "Men's Cut"),
        ('wcut', "Women's Cut"),
        ('col', 'Coloring'),
        ('wax', 'Waxing'),
        ('high', 'Highlights'),
        ('con', 'Conditioning'),
        ('bride', 'Bridal'),
        )
    skills = MultiSelectField(
        max_choices=7,
        choices=hair_skills,
        default=(('None'))
    )

    def __str__(self):
        return str(self.user)

@receiver(post_save, sender=User)
def create_professional(sender, instance, created, **kwargs):
    if created:
        Professional.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_professional(sender, instance, **kwargs):
    instance.professional.save()



# class TempCustomer(models.Model):
#     #user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
#     zip_code = models.CharField(max_length=30)

#     type_of_hair_job = models.CharField(max_length=12, choices=hair_choices, default="None")
#     # type_of_nail_job = models.CharField(max_length=20, choices=nail_choices, default="None")
#     # type_of_well_job = models.CharField(max_length=12, choices=hair_choices, default="None")
#     #time_of_job = models.DateField(default="2021-10-03")
#     #time_of_job = models.TimeField(default="")
    
    # def __str__(self):
    #     return str(self.user)

# @receiver(post_save, sender=User)
# def create_customer(sender, instance, created, **kwargs):
#     if created:
#         TempCustomer.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_customer(sender, instance, **kwargs):
#     instance.tempcustomer.save()