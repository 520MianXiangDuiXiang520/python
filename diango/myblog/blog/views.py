from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return render(request,'blog/dia1.html')

# Create your views here.
