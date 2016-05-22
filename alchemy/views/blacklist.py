from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from alchemy.models import *


def blacklist(request, blackemail):
	if not request.user.is_authenticated():	
		return render(request, 'index.html')
	
	context = {}
	email2blacklist = get_object_or_404(popEmails, id=blackemail)
	
	if request.method == "POST":
		EmailInSpam, EmailInSpamCreated = spamAddress.objects.get_or_create(emailAddress=str(email2blacklist.fromEmail).lower(), emailHash=email2blacklist.emailHash, ipAddress=email2blacklist.senderip)
		EmailInSpam.score += 1
		EmailInSpam.save()
		
		if EmailInSpamCreated:
			EmailInSpam.addedByUser.add(request.user)
		
		if email2blacklist.whitelist:
			email2blacklist.whitelist = False
		
		email2blacklist.blacklist = True
		email2blacklist.save()
		return HttpResponseRedirect('/dashboard')
	
	context['email2blacklist'] = email2blacklist
	
	return render(request, 'blacklist.html', context)