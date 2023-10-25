from django.shortcuts import render, redirect

from .forms import CreateUserForm



from django.contrib.auth import get_current_site
from . token import user_tokenizer_generate


from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode



# Create your views here.

def register(request):
    
    form = CreateUserForm()
    
    if request.method == 'POST':
        
        form = CreateUserForm(request.POST)
        
        if form.is_valid():
            
            # form.save()
            
            # return redirect('store')
            
            user = form.save()
            
            user.is_activee = False
            
            user.save()
            
            # Email verification setup (template)
            
            current_site = get_current_site(request)
            
            subject = 'Account verification email'
            
            message = render_to_string('account/registration/email-verification.html', {
                                
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': user_tokenizer_generate.make_token(user),
                            
            })
            
            user.email_user(subject=subject, message=message)
            
            
            return redirect('email-verification-sent')
        
    context = {'form': form}
    
    return render(request, 'account/registration/register.html',context=context)



def email_varification(request):
    
    pass


def email_varification_sent(request):
    
    pass


def email_varification_success(request):
    
    pass


def email_varification_failed(request):
    
    pass

