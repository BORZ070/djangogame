from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render
from account.forms import LoginForm

# def login_views(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             user = authenticate(request, username=username, password=password)
#         if user is not None:
#             if user.is_active:
#                 login(request, user)
#                 return HttpResponse('authenticate successful')
#             else:
#                 return HttpResponse("user don't active")
#         else:
#             return HttpResponse("user don't found")
#     else:
#         form = LoginForm()
#
#     return render(request, 'registration/login.html', {'form':form})


def index_views(request):
    return render(request, 'index_page.html')