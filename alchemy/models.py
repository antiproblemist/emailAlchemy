from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class userEmail(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)
	email = models.CharField(max_length=100, blank=False, null=False)
	password = models.CharField(max_length=100, blank=False, null=False)	
	incomingMailServer = models.CharField(max_length=100, blank=False, null=False)
	incomingPort = models.IntegerField(blank=False, null=False)
	requiresSSL = models.BooleanField(default=True)
	lastSynced = models.DateTimeField(blank=True, null=True)

class popEmails(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)
	userEmail = models.ForeignKey(userEmail, on_delete=models.CASCADE, blank=False, null=False)
	subject = models.CharField(max_length=200, blank=True, null=True)
	fromEmail = models.CharField(max_length=100, blank=True, null=True)
	toEmail = models.CharField(max_length=100, blank=True, null=True)
	dateEmail = models.CharField(max_length=100, blank=True, null=True)
	senderip = models.CharField(max_length=100, blank=True, null=True)
	rawMessage = models.TextField(blank=True, null=True)
	emailHash = models.CharField(max_length=100, blank=True, null=True)
	isSpam = models.BooleanField(default=False)
	whitelist = models.NullBooleanField(blank=True, null=True)
	blacklist = models.NullBooleanField(blank=True, null=True)
	
class spamAddress(models.Model):
	emailAddress = models.CharField(max_length=100, blank=True, null=True)	
	emailHash = models.CharField(max_length=100, blank=True, null=True)
	ipAddress = models.CharField(max_length=100, blank=True, null=True)
	score = models.IntegerField(blank=False, null=False, default=0)
	notSpamVotes = models.IntegerField(blank=False, null=False, default=0)
	addedByUser = models.ManyToManyField(User)

class spamwords(models.Model):
	spamkeywords = models.TextField(blank=True, null=True)
