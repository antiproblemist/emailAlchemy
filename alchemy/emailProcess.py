import poplib
from email import parser
from django.http import HttpResponseRedirect
from django.conf import settings
import re
import hashlib
from dateutil.parser import parse, tz
from datetime import datetime, tzinfo
import os, os.path


class emailProcess(object):
	
	def __init__(self):
		pass
	
	def extractEmail(self, raw):
		if '<' in raw and '>' in raw:
			emails = re.findall(r'<(.*)>', raw)
			if emails:
				cs_emails = (',').join(emails)
				return cs_emails
		else:
			return raw
			
	def extractIP(self, raw):
		if '[' in raw and ']' in raw:
			ip = re.findall(r'\[([0-9.]*)\]', raw)
			if ip:
				ip = (',').join(ip)
				return ip
		else:
			return raw
	
	def emailAuthenticate(self, incoming):
		try:
			if incoming['sslReq']:
				pop_conn = poplib.POP3_SSL(incoming['incServer'], int(incoming['incPort']))
			else:
				pop_conn = poplib.POP3(incoming['incServer'], int(incoming['incPort']))
			pop_conn.user(incoming['email'])
			pop_conn.pass_(incoming['password'])
			pop_conn.quit()
		except poplib.error_proto as e:
			return 0
		return 1
	
	def makedir_p(self, path):
		if not os.path.exists(os.path.dirname(path)):
			try:
				os.makedirs(path)
			except OSError as exc:
				if exc.errno != errno.EEXIST:
					raise
	
	def getEmails(self, incoming, folderid):
		try:
			if incoming['sslReq']:
				pop_conn = poplib.POP3_SSL(incoming['incServer'], int(incoming['incPort']))
			else:
				pop_conn = poplib.POP3(incoming['incServer'], int(incoming['incPort']))
			pop_conn.user(incoming['email'])
			pop_conn.pass_(incoming['password'])
			messages = [pop_conn.retr(i) for i in range(1, len(pop_conn.list()[1]) + 1)]
			messages = ["\n".join(mssg[1]) for mssg in messages]
			messages = [parser.Parser().parsestr(mssg) for mssg in messages]
			retMessages = {}
			for i, message in enumerate(messages):
				retMessagesDisect = {}
				retMessagesDisect['from'] = self.extractEmail(str(message['from']))
				retMessagesDisect['to'] = self.extractEmail(str(message['to']))
				retMessagesDisect['subject'] = message['subject']
				msgDate = parse(message['date'])
				to_zone = tz.tzlocal()
				msgDate = msgDate.replace(tzinfo=to_zone)
				retMessagesDisect['date'] = msgDate
				retMessagesDisect['ip'] = self.extractIP(message['received'])
				retMessagesDisect['rawMsg'] = message
				retMessagesDisect['hash'] = hashlib.md5(str(message)).hexdigest()
				
				self.makedir_p(getattr(settings, 'MEDIA_ROOT', None) + '\\' + str(folderid) + '\\')
				file = open(getattr(settings, 'MEDIA_ROOT', None) + '\\' + str(folderid) + '\\' + str(retMessagesDisect['hash']) + '.eml', 'w')
				file.write(str(message))
				file.close()
				
				retMessages[str(i)] = retMessagesDisect
			pop_conn.quit()
		except poplib.error_proto as e:
			return 0
		return retMessages
	
		
		
		
		