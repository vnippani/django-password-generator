from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.
def home(request):
	return render(request,'generator/home.html')

def password(request):

	thepassword = 'testing'
	characters = list('abcdefghijklmnopqrstuvwxyz')
	#get stuff from the request (the form that was sent in)

	length = int(request.GET.get('length',14)) #get info from the form, default length = 14
	if request.GET.get('uppercase'):
		characters.extend('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
	if request.GET.get('numbers'):
		characters.extend('0123456789')
	if request.GET.get('special'):
		characters.extend('!@#$%^&*')	
	special = request.GET.get('special')
	numbers = request.GET.get('numbers')

	password = ''
	for i in range(0,length):
		password += random.choice(characters)


	return render(request,'generator/password.html',{'password':password})

def about(request):
	return render(request,'generator/about.html')
