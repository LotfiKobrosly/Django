from django.db import models

# Create your models here.

class Transaction(models.Model):
	date = models.DateTimeField("Date")
	source = models.CharField("From", max_length=64 , default="", blank=True)
	hashCode = models.CharField("Hash", max_length=64 , default="", blank=True)
	destination = models.CharField("To", max_length=64 , default="", blank=True)
	
	
	def __str__(self):
		return self.hashCode
	
	def dateOfTransaction(self):
		return self.date
	
	
	
class Block(models.Model):
	date=models.DateTimeField("Date")
	hashCode=models.CharField("Hash", max_length=64, default="", blank=True)
	transactions=[]
	previous=Block
	
	
	def __str__(self):
		return self.hashCode
	
	def dateOfValidation(self):
		return self.date
	
	def previousBlock(self):
		return self.previous.__str__
