from django.db import models

# Create your models here.
class TraducaoMorse(models.Model):
    morse = models.TextField(max_length=1000)
    texto = models.TextField(max_length=500)

    def __str__(self):
        return self.morse + ' -> ' + self.texto


class TraducaoTexto(models.Model):
    texto = models.TextField(max_length=1000)
    morse = models.TextField(max_length=2500)

    def __str__(self):
        return self.texto + ' -> ' + self.morse
