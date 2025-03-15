from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=50)
    idade =  models.IntegerField()
    mensagem = models.TextField(max_length=255)
    
    def __str__(self):
        return f'O usuario {self.nome}, tem {self.idade} de idade e manda a seguinte mensagem {self.mensagem}'
