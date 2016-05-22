from django.shortcuts import render
from django.http import HttpResponseRedirect
from alchemy.models import *
from django.shortcuts import get_object_or_404

def delUserEmail(request, deluseremail):
	if not request.user.is_authenticated():	
		return render(request, 'index.html')
	
	context = {}
	email2delete = get_object_or_404(userEmail, id=deluseremail, user=request.user)
	if request.method == "POST":
		email2delete.delete()
		return HttpResponseRedirect('/dashboard')
	
	context['email2delete'] = email2delete
	
	return render(request, 'delete.html', context)