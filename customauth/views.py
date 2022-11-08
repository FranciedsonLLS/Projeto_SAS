from django.shortcuts import redirect, render
from .forms import *
from .decorators import logout_required
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate 
from django.contrib.auth import login as make_login
from django.contrib.auth import logout as make_logout
from django.contrib.auth.decorators import login_required

# Create your views here.
# @logout_required
def register(request):
    if request.user.is_authenticated:
        return redirect_default(settings.LOGIN_REDIRECT_URL)
    else:
        form = UserCreationForm(request.POST or None)
        if form.is_valid():     
            form.save()
            messages.success(request, "Sua conta foi criada com sucesso!")
            user = authenticate(username=form.cleaned_data['email'], password=form.clean_password2)
            if user is not None:
                make_login(request, user)
            return redirect_default(settings.LOGIN_REDIRECT_URL)
        return render(request, 'auth/register.html', { 'form': form })

# @logout_required
def login(request):
    if request.user.is_authenticated:
        return redirect_default(settings.LOGIN_REDIRECT_URL)
    else:
        form = AuthenticationForm(request.POST or None)        
        if request.method == 'POST':
            print('é post')
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(username=email, password=password)            
            messages.success(request, "Login feito com sucesso!")
            print('usuário: ' + str(user))
            if user is not None:
                print('login feito')
                make_login(request, user)
                return redirect_default(settings.LOGIN_REDIRECT_URL)
        return render(request, 'auth/login.html',  { 'form': form })

@login_required
def logout(request):
    make_logout(request)
    return redirect_default(settings.LOGOUT_REDIRECT_URL)

def redirect_default(ref):
    print(ref)
    if ref:
        try:
            # redirect to ref view name if valid
            return redirect(ref)
        except:
            print('No reverse match found')

    # redirect to specific view if ref is invalid
    return redirect('/')
