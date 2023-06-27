from django.shortcuts import render, redirect
from allauth.account.views import LoginView,LogoutView,SignupView
from .forms import SignupForm
from django.urls import reverse_lazy

class Login(LoginView):
    template_name = "accounts/login.html"

class Logout(LogoutView):
    template_name = "accounts/logout.html"

    def post(self,*args,**kwargs):
        if self.request.user.is_authenticated:
            self.logout()
        return redirect("home")

class Signup(SignupView):
    form_class = SignupForm
    template_name = "accounts/signup.html"
    success_url = reverse_lazy("index")