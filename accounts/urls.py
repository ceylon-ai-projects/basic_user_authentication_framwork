# pages/urls.py
from django.urls import path

from accounts.views import ProfilePageView

# def auto_redirect(request):
#     if request.user.is_authenticated:
#         return views.SignUp
#
#     return views.HomePageView
urlpatterns = [
    path('', ProfilePageView.as_view(), name="Home"),
]
