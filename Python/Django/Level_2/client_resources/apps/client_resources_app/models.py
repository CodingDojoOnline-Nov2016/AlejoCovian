from __future__ import unicode_literals

from django.db import models
import re
reg = re.compile("(\(?\d{3}\D{0,3}\d{3}\D{0,3}\d{4}).*?")

# Create your models here.
class ClientManager(models.Manager):
	def create_client(self, business_name, email, phone, notes):
		client = self.create(
			business_name=business_name,
			email=email, 
			phone=phone, 
			notes=notes,
			)
		return (True, client)

	def validate_and_add(self, data):
		errors = []
		business_name = data['business_name']
		email = data['email']
		phone = data['phone']
		notes = data['notes']
		if len(business_name)<1:
			errors.append('Business name cannot be left blank.')
		if len(email)<1:
			errors.append('Email cannot be left blank.')
		if len(phone)<1:
			errors.append('Phone cannot be left blank.')
		if not reg.match(phone):
			errors.append('Must be a valid phone number.')
		if len(notes)<1:
			errors.append('Notes cannot be left blank.')
		else:
			client = self.create_client(business_name, email, phone, notes)
			return (True, client)



class Client(models.Model):
	business_name = models.CharField(max_length=125)
	email = models.CharField(max_length=255)
	phone = models.CharField(max_length=25)
	notes = models.CharField(max_length=1000)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	objects = ClientManager()

#######

class ProjectManager(models.Manager):

	def create_project(self, project, notes, project_client):
		project = self.create(project=project, notes=notes, project_client=project_client)
		return (True, project)

	def validate_and_add(self, data):
		project = data['project']
		notes = data['notes']
		project_client = Client.objects.get(id=data['client_id'])
		errors = []
		if len(project)<1:
			errors.append('project name cannot be left blank.')
		if len(notes)<1:
			errors.append('please add some content to the notes field')
		if errors:
			return (False, errors)
		else:
			project = self.create_project(project, notes, project_client)
			return (True, project)

class Project(models.Model):
	project = models.CharField(max_length=125)
	notes = models.CharField(max_length=1000)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	project_client = models.ForeignKey(Client)

	objects = ProjectManager()
	