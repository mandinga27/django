from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#creando base de datos con una class
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    adress = models.CharField(max_length=30)
    birthday = models.DateField()
    gender =models.CharField(max_length=1,
                             choices=(
                                 ('H', "Hombre"),
                                 ('M', "Mujer"),
                                 ('S', "Sin Especificar")
                             ))
    phone = models.IntegerField()
    description =models.TextField()
    #tabla intermedia ->relacion



class UserLanguage(models.Model):
    userprofile = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
    language = models.ForeignKey('Language', on_delete=models.CASCADE)


#el campo 'userprofile y languaje son unicos
class Meta:
    unique_together = ((''), 'userprofile', 'Languaje')


class Language(models.Model):
    name = models.CharField(max_length=20, primary_key=True)