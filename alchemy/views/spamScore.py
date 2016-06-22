from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from alchemy.models import *
from django.shortcuts import get_object_or_404
from django.db.models import Q

import os, os.path
from django.conf import settings
import json

def spamScore(request, selecteduemail):
	if not request.user.is_authenticated():	
		return render(request, 'index.html')
		
	useremail = get_object_or_404(userEmail, id=selecteduemail)
	
	selEmails = popEmails.objects.filter(user=request.user, userEmail=useremail)
	
	keywords = spamwords.objects.first()
	
	if not keywords:
		file = open(os.path.join(getattr(settings, 'BASE_DIR', None), "alchemy",'spamwords.js'), 'r+')
		keywordsFromFile = json.load(file)
		file.close()		
		keywords = ','.join(keywordsFromFile['keywords'])
		spamwords.objects.create(spamkeywords=keywords)
	else:
		keywords = keywords.spamkeywords.split(',')
	
	for email in selEmails:
		
		EmailInSpam = spamAddress.objects.filter(Q(emailHash=email.emailHash))
		
		#Check if email hash is already saved in spam table
		# if yes then increase the email, address, ip score by 1
		if EmailInSpam:
			EmailInSpam, EmailInSpamCreated = spamAddress.objects.get_or_create(emailAddress=str(email.fromEmail).lower(), emailHash=email.emailHash, ipAddress=email.senderip)
			EmailInSpam.score += 1
			EmailInSpam.save()
			if EmailInSpamCreated:
				EmailInSpam.addedByUser.add(request.user)
			
			if EmailInSpam.score > EmailInSpam.notSpamVotes:
				email.isSpam = True
				email.save()
				
		#if not then calculate the score 
		else:
			sp_score = 0
			for word in keywords:
				if word in email.rawMessage:
					print str(word)
					sp_score +=1
			#print str(email.fromEmail) + " score " + str(sp_score)
			if sp_score > 5:
				#Lenient
				EmailInSpam, EmailInSpamCreated = spamAddress.objects.get_or_create(emailAddress=str(email.fromEmail).lower(), emailHash=email.emailHash, ipAddress=email.senderip)
				EmailInSpam.score += 1
				EmailInSpam.save()
				if EmailInSpamCreated:
					EmailInSpam.addedByUser.add(request.user)
							
				if EmailInSpam.score > EmailInSpam.notSpamVotes:
					email.isSpam = True
					email.save()
			else:
				print str(email.fromEmail) + "	is not spam"
				email.isSpam = False
				email.save()
	
	return HttpResponseRedirect('/dashboard')