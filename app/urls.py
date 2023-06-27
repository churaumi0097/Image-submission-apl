from django.urls import path 
from .views import (
    Home,Index,Detail,Create,Delete,Update
)

urlpatterns = [
    path("",Home.as_view(),name = "home"),
    path("index",Index.as_view(),name = "index"),
    path("index/detail/<int:pk>",Detail.as_view(),name = "detail"),
    path("index/create/",Create.as_view(),name = "create"),
    path("index/delete/<int:pk>",Delete.as_view(),name = "delete"),
    path("indexupdate/<int:pk>",Update.as_view(),name = "update"),
]