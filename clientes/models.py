from django.db import models


class Cliente(models.Model):

    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    cpf_cnpj = models.CharField(max_length=14)

    def __str__(self):
        return self.nome


class OrdemServico(models.Model):

    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    equipamento = models.CharField(max_length=40)
    descricao = models.TextField()
    status = models.CharField(max_length=20)
    data_abertura = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.equipamento