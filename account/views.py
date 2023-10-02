from django.shortcuts import render
from account.forms import LoginForm

def login_views(request):
    form = LoginForm()
    return render(request, 'registration/login.html', {'form':form})


