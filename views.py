from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def home(request):

	return render(request, 'notes/dashboard.html')



def Language(request):
	

	return render(request, 'notes/Language.html', )

def Snippet(request):
	Snippet = snippet.object.all()
	return render(request, 'notes/user.html', {'Snippet':Snippet})



