from django.shortcuts import render
from django.http import HttpResponse

def testt(request):
    return HttpResponse('Все хорошо')
