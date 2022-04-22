from django.db import models

# Create your models here.


class NomeFilme(models.Model):
    nome_filme = models.CharField(max_length=50)

    def __str__(self):
        return self.nome_filme