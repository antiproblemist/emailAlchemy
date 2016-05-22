from django.shortcuts import render
from django.utils.html import strip_tags
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect

def index(request):
	if not request.user.is_authenticated():
		return render(request, 'index.html')
	else:
		context['is_authenticated'] = True

	if request.method == "POST" and 'login-email' in request.POST:
		fields = {}
		fields['email'] = strip_tags(request.POST.get('login-email','')).strip()
		fields['password'] = strip_tags(request.POST.get('login-password','')).strip()

		for field, value in fields.items():
			if not value:
				return render(request, 'index.html', {'error':'Please do not leave any fields blank'})

		user = authenticate(username=fields['email'], password=fields['password'])
		if user is not None:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect('/dashboard')
			else:
				return render(request, 'index.html', {'error':'Your account has been disabled'})
		else:
			return render(request, 'index.html', {'error':'The username or password is incorrect'})
	return render(request, 'index.html')
