from django.shortcuts import render, get_object_or_404
from alchemy.models import *

def showUserSelectedEmails(request, selecteduemail):
	context = {}
	if not request.user.is_authenticated():	
		return render(request, 'index.html')
	else:
		context['is_authenticated'] = True
	
	uemails = userEmail.objects.filter(user=request.user)
	if uemails:
		context['uemails'] = uemails
		
	useremail = get_object_or_404(userEmail, id=selecteduemail)
	
	selEmails = popEmails.objects.filter(user=request.user, userEmail=useremail).order_by('-dateEmail')
	
	context['selemails'] = selEmails
	context['sue'] = int(selecteduemail)
	return render(request, 'dashboard.html', context)