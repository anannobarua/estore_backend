from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django import forms


class CreateUserForm(UserCreationForm):
    
    class Meta:
        
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
        
    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)
        
        # Make email as required
        self.fields['email'].required = True
        
    
    # Email validation
        
    def clean_email(self):
        
        email = self.cleaned_data.get("email")
        
        if User.objects.filter(email=email).exists():
            
            raise forms.ValidationError('This Mail in Invalid')
        
        
        # Len Function updated ### 
        
        if len(email) >= 350:
            
            raise forms.ValidationError("Your Email is TOO Long")
        
         
        return email

# from collections import UserString
# from django.contrib.auth.forms import UserCreationForm
# from django import forms

# class CreateUserForm(UserCreationForm):
    
#     def __init__(self, *args, **kwargs):
#         super(CreateUserForm, self).__init__(*args, **kwargs)
        
#         # Make email as required
#         self.fields['email'].required = True
        
#     # Email validation
#     def clean_email(self):
#         email = self.cleaned_data.get("email")
        
#         if UserString.objects.filter(email=email).exists():
#             raise forms.ValidationError('This email is already in use.')
        
#         if len(email) >= 350:
#             raise forms.ValidationError("Your email is too long.")
         
#         return email
