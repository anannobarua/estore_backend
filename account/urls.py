from django.urls import path

from . import views  

urlpatterns = [
    
    path('register', views.register, name='register'),
    
    # Email Varification URLS
    # for Dynamic URLS we use the < 
    
    path('email-verification/<str:uidb64>/<str:token>/', views.email_verification, name='email-verification'),
      
    path('email-verification-sent', views.email_varification_sent, name='email-verification-sent'),
    
    path('email-verification-success', views.email_varification_success, name='email-verification-success'),
    
    path('email-verification-failed', views.email_varification_failed, name='email-verification-failed'),
    
    
    
    
]
