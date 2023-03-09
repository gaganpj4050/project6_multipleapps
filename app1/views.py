from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def dhoni(request):
    return HttpResponse('<h1>Dhoni is best finisher in the world</h1>')

def raina(request):
    return HttpResponse('<h1>raina is known as MR ipl in india</h1>')

