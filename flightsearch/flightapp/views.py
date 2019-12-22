from django.shortcuts import render
#from django import forms
from .forms import flight_details
# Create your views here.
def index(request):
	form=flight_details()
	context={'form':form}
	return render(request,'index.html',context)
#def search()