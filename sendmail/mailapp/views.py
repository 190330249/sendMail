from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail

def home(request):

    return render(request, 'home.html')

def sendmail(request):

    send_mail(
        'Subject',
        'Email message',
        'Nithya.kl.Official@gmail.com',
        ['190330171@klh.edu.in','ravitejakompalli01@gmail.com'],
        fail_silently=False,
    )

    return HttpResponse('Mail successfully sent')

# Create your views here.
