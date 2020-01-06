from django.db import models

class smarteagle(models.Model):
    temperatura = models.IntegerField()
    datadeleitura = models.DateTimeField(auto_now_add=True)
