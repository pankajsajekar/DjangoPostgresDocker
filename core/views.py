from django.shortcuts import render
from django.http import HttpResponse

from core.models import Student
from testdocker.common.emails.send_email_otp import send_email_otp
from random import randint 

# Create your views here.
def home(request):
    students = Student.objects.all()
    return HttpResponse("<h1>Home Page<h1>")

def SendEmail(request):
    otp = randint(1000, 9999)
    print(otp)
    email = 'pankaj@arcitech.ai'
    send_email_otp(otp, email)
    return HttpResponse("Send Email")
    # return render(request, 'base.html')