from django.db import models

# Create your models here.
#class Status(models.Model):
#	aciertos = models.IntegerField()
#	pistas_dadas = models.IntegerField()
#	tiempo = models.IntegerField()
	
class send_points(models.Model):
	token = models.CharField(max_length=200)
	validation = models.CharField(max_length=200)
	invitation = models.CharField(max_length=200)
	percent = models.CharField(max_length=200)
	
class PointsT(models.Model):
	token = models.CharField(max_length=200)
	validation = models.CharField(max_length=200)
	invitation = models.CharField(max_length=200)
	percent = models.CharField(max_length=200)
	
	
class objetoTest(models.Model):
	objeto = models.CharField(max_length=200)