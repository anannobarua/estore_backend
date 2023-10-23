from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User

from django import forms


class CreateUserForm(UserCreationForm):
    
    class Meta:
        
        model = User
        fields = ['username', 'email', 'password', 'password2']
        
        
    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)
        
    
    # Email validation
        
    def clean_email(self):
        
        email = self.cleaned_data.get("email")
        
        if User.objects.filter(email=email).exists():
            
            raise forms.ValidationError('This Mail in Invalid')
        
        if len(email >= 350):
            
            raise forms.ValidationError("Your Email is TOO Long")