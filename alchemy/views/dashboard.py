from django.shortcuts import render
from alchemy.models import *
from django.http import HttpResponseRedirect

def dashboard(request):
	context = {}
	if not request.user.is_authenticated():	
		return HttpResponseRedirect('/')
	else:
		context['is_authenticated'] = True

	uemails = userEmail.objects.filter(user=request.user)
	if uemails:
		context['uemails'] = uemails

	return render(request, 'dashboard.html', context)
