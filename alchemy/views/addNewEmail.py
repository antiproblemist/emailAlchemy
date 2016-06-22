from django.shortcuts import render
from django.utils.html import strip_tags
from django.http import HttpResponseRedirect
from alchemy.models import *
from alchemy.emailProcess import emailProcess

def addNewEmail(request):
	if not request.user.is_authenticated():	
		return render(request, 'index.html')
	
	if request.method == "POST" and 'addnewemail-email' in request.POST:
		fields = {}
		fields['email'] = strip_tags(request.POST.get('addnewemail-email','')).strip()
		fields['password'] = strip_tags(request.POST.get('addnewemail-password','')).strip()
		fields['incServer'] = strip_tags(request.POST.get('addnewemail-incomingserver','')).strip()
		fields['incPort'] = strip_tags(request.POST.get('addnewemail-incomingport','')).strip()
		fields['sslReq'] = strip_tags(request.POST.get('addnewemail-sslreq','')).strip()
		
		for field, value in fields.items():
			if not value:				
				return render(request, 'addNewEmail.html', {'error':'Please do not leave any fields blank'})
		
		if fields['sslReq'] == 'yes':
			fields['sslReq'] = True
		elif fields['sslReq'] == 'no':
			fields['sslReq'] = False
		
		print fields
		
		ep = emailProcess()
		connEst = ep.emailAuthenticate(fields)
		if not connEst:
			return render(request, 'addNewEmail.html', {'error':'Authentication failed. Please check details and try again'})
		else:
			uemail = userEmail.objects.create(user=request.user, email=fields['email'], password=fields['password'], incomingMailServer=fields['incServer'], incomingPort=fields['incPort'], requiresSSL=fields['sslReq'])
			if uemail:
				uemail = userEmail.objects.get(id=uemail.id)
				print uemail
				emails = ep.getEmails(fields, uemail.id)
				if emails:
					for i, e in emails.items():						
						popEmails.objects.create(user=request.user, userEmail=uemail, subject=e['subject'], fromEmail=e['from'], toEmail=e['to'], dateEmail=e['date'], rawMessage=e['rawMsg'], senderip=e['ip'], emailHash=e['hash'])
				return HttpResponseRedirect('/dashboard')
	
	return render(request, 'addNewEmail.html')