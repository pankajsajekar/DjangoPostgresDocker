from django.core.mail import send_mail
from testdocker.settings import EMAIL_HOST_USER
from django.template.loader import render_to_string

def send_email_otp(OTP, to_email):
    email_content = render_to_string('transactional/send_email_otp.html', {'OTP': OTP})

    send_mail(
        subject = f'Your OTP for testing',
        message='',
        html_message=email_content,
        from_email=EMAIL_HOST_USER,
        recipient_list=[to_email],
        fail_silently=False
    )
