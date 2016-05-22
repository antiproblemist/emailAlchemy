from django.shortcuts import render, get_object_or_404
from alchemy.models import *

def reademail(request, reademail):
	context = {}
	if not request.user.is_authenticated():	
		return render(request, 'index.html')
	else:
		context['is_authenticated'] = True
	
	selEmail = get_object_or_404(popEmails, id=reademail, user=request.user)
	
	context['reademail'] = selEmail
	return render(request, 'reademail.html', context)