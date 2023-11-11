from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib.auth.models import User 
from django.contrib.auth import login, authenticate, logout 
from django.conf import settings
from django.core.mail import send_mail

def send_registration_email(user_email, user_first_name):
    subject = 'Welcome to Our Website!'
    message = f"Dear {user_first_name},\n\nThank you for registering on our website. We hope you enjoy your experience!"
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [user_email]
    send_mail(subject, message, from_email, recipient_list)


def reg(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the user registration data
            #send_registration_email(user.email,user.username)  # Send confirmation email
            return redirect("reg.html")
    

