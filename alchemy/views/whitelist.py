from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from alchemy.models import *


def whitelist(request, whiteemail):
	if not request.user.is_authenticated():	
		return render(request, 'index.html')
	
	context = {}
	email2whitelist = get_object_or_404(popEmails, id=whiteemail)
	
	if request.method == "POST":
		addressInSpam = spamAddress.objects.get(emailAddress=str(email2whitelist.fromEmail).lower())
		if addressInSpam.notSpamVotes:
			addressInSpam.notSpamVotes += 1
		else:
			addressInSpam.notSpamVotes = 1
		addressInSpam.save()
		
		if email2whitelist.blacklist:
			email2whitelist.blacklist = False

		email2whitelist.whitelist = True
		email2whitelist.save()
		return HttpResponseRedirect('/dashboard')
	
	context['email2whitelist'] = email2whitelist
	
	return render(request, 'whitelist.html', context)