from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from account.forms import LoginForm, UserRegistrationForm, UserEditForm, ProfileEditForm
from account.models import Profile
from django.contrib import messages
from games.models import Game
from articles.models import Article

from tbot.forms import SupportQForm


def index_views(request):
    cards_game = Game.objects.all().order_by('?')[:6]
    cards_article = Article.objects.all().order_by('?')[:6]
    if request.method == 'POST':
        form = SupportQForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = SupportQForm()

    return render(request, 'index.html', {'form':form, 'cards_game':cards_game, 'cards_article':cards_article})

@login_required
def dashboard(request):
    return render(request, 'account/dashboard.html')


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            Profile.objects.create(user=new_user)
            return render(request, 'account/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'account/register.html', {'user_form':user_form})


@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
        # profile_form = ProfileEditForm(instance=request.profile.user, data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Success edit profile')
        else:
            messages.error(request, 'Update error')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
        # profile_form = ProfileEditForm(instance=request.profile.user)
    return render(request, 'account/edit.html', {'user_form':user_form, 'profile_form':profile_form})


def uuid_validater(request, uuid):

    profile = Profile.objects.filter(uuid=uuid).exists()
    return HttpResponse(profile)







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

