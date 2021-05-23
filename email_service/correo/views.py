from django.shortcuts import render
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect

from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import json

@csrf_exempt
def send_email(request):
    #subject = request.data['subject'] 
    body_byte = request.body
    body_str = body_byte.decode('utf-8')
    body_json = json.loads(body_str)
    destino = body_json['email']
    subject = body_json['subject']
    message = body_json['message']
    #print(destino,subject,message)
    if subject and message and destino:
        try:
            send_mail(subject=subject, message=message,from_email=settings.EMAIL_HOST_USER,recipient_list=[destino])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return HttpResponse('Correo Enviado')
    else:
        
        return HttpResponse('Make sure all fields are entered and valid.')
