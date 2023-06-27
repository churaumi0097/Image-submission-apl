from django.urls import path
from .views import Login,Logout,Signup

urlpatterns = [
    path("login/",Login.as_view(),name = "account_login"),
    path("logout/",Logout.as_view(),name="account_logout"),
    path("signup/",Signup.as_view(),name = "account_signup")
]