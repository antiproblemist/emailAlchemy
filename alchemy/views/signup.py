from django.shortcuts import render
from django.utils.html import strip_tags
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.http import HttpResponseRedirect

def signup(request):	
	if request.method == "POST" and 'signup-email' in request.POST:
		fields = {}
		fields['email'] = strip_tags(request.POST.get('signup-email','')).strip()
		fields['password'] = strip_tags(request.POST.get('signup-password','')).strip()
		fields['repassword'] = strip_tags(request.POST.get('signup-repassword','')).strip()
		
		if fields['password'] != fields['repassword']:
			return render(request, 'signup.html', {'error':'Password and re enter password do not match'})
			
		for field, value in fields.items():
			if not value:				
				return render(request, 'signup.html', {'error':'Please do not leave any fields blank'})
		
		try:
			user = User.objects.create_user(username=fields['email'], email=fields['email'], password=fields['password'])
		except IntegrityError:
			return render(request, 'signup.html', {'error':'Email already exists'})
			
		if user:
			return HttpResponseRedirect('/')
			
	return render(request, 'signup.html')
