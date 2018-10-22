# pages/urls.py
from django.shortcuts import render
from django.urls import path

from pages.views import HomePageView,IndexPageView
from . import views


# def auto_redirect(request):
#     if request.user.is_authenticated:
#         return views.SignUp
#
#     return views.HomePageView


urlpatterns = [
    path('home', HomePageView.as_view(), name="Home"),
    path('', IndexPageView.as_view(), name="Index"),
]
