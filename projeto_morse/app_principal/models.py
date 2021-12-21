from django.db import models

# Create your models here.
class Traducao(models.Model):
    morse = models.CharField(max_length=500)
    texto = models.CharField(max_length=500)

    def __str__(self):
        return self.morse + ' -> ' + self.texto
