from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
	return render(request,'personal/home.html')

def contact(request):
	return render(request,'personal/contacts.html',{'content' : ['email me @' , 'nirparai@yahoo.com']})
	