
from django.urls import path
from .views import SendEmail, home


urlpatterns = [
    path("", home, name="home"),
    path("sendemail/", SendEmail, name="SendEmail"),
]

