from django.db import models

class ChimModel(models.Model):
    chimcuaai=models.CharField(max_length=100)
    email=models.CharField(max_length=150)
    docong=models.IntegerField()
    dodai=models.IntegerField()
    sizechim=models.CharField(max_length=100)