
from django.http import HttpResponse
import requests
import datetime

def index(request):
    return HttpResponse("Hello, world.")

def welcome(request):
    return HttpResponse("welcome to my project")

def current_datetime(request):                  #exmaple for current datetime using get request
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)