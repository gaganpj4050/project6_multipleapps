from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def virat(request):
    return HttpResponse('<h2>Virat is a best BATSMAN in the World</h2>')

def abd(request):
    return HttpResponse('<h1>ABD is a MR 360 in the ipl</h1>')