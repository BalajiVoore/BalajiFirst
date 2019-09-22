from django.shortcuts import render
from .models import personal
# Create your views here.
def myself(request):
    per=personal.objects
    return render(request,'personal.html',{'per':per})
