from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import RegistrationForm, AccountAuthenticationForm, AccountUpdateForm
from .models import Account
from django.contrib.auth.decorators import login_required


def registration_view(request):
    if request.POST:
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            # getting data for login

            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            return redirect('delight:index')
        else:
            context = {'registration_form': form}
    else:
        form = RegistrationForm()
        context = {'registration_form': form}
    return render(request, 'account/register.html', context)


def logout_view(request):
    logout(request)
    return redirect('delight:index')


def login_view(request):

    context = {}

    user = request.user
    if user.is_authenticated:
        return redirect('account:login')

    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)

            if user:
                login(request, user)
                return redirect('delight:index')
    else:
        form = AccountAuthenticationForm()

    context['login_form'] = form
    return render(request, 'account/login.html', context)



# @login_required()
# def my_profile(request):
#     profile = Account.objects.filter(username=request.user)
#     items = Item.objects.filter(owner=request.user)
#     context = {'profile': profile, 'items': items}
#     return render(request, 'store_information/my_profile.html', context)


def account_view(request):
    if not request.user.is_authenticated:
        return redirect("account:login")

    context = {}

    if request.POST:
        form = AccountUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            context['success_message'] = "Updated!"
    else:
        form = AccountUpdateForm(
            initial={
                "email": request.user.email,
                "username": request.user.username,
            }
        )
    context['account_form'] = form
    return render(request, 'account/account.html', context)
