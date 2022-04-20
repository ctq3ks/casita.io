from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('signout/', views.signout, name='signout'),
    path('pro_home/', views.pro_home, name='pro-home'),
    path('customer_survey/', views.customer_survey, name='customer-survey'),
    path('hair_pros/', views.hair_pros, name='hair-pros'),

]