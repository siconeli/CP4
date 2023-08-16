from django.db import models


class Base(models.Model):
    criados = models.DateField('Criação', auto_now_add=True)
    modificado = models.DateField('Atualização', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True

    
class UnidadeFederativa(Base):
    uf = models.CharField(max_length=50) 

    def __str__(self):
        return f'{self.uf}'


class ProcessoAdministrativo(Base):
    pat = models.IntegerField() #PAT n°
    munic = models.CharField(max_length=50, verbose_name='Município') #Município
    uf = models.ForeignKey(UnidadeFederativa, on_delete=models.PROTECT)
    datini = models.DateField() #Data inicial
    datfin = models.DateField() #Data final
    datdivat = models.DateField() #Data dívida ativa
    valtrib = models.DecimalField(decimal_places=2 , max_digits=9) #Valor do Tributo
    valmul = models.DecimalField(decimal_places=2 , max_digits=9) #Valor da Multa
    valcred = models.DecimalField(decimal_places=2 , max_digits=9) #Valor do Crédito
    valatu = models.DecimalField(decimal_places=2 , max_digits=9) #Valor do Atualizado
    datvalatu = models.DateField() #Data valor atualizado
    datand = models.DateField() #Data andamento
    anda = models.IntegerField() #Andamento atual
    datprazo = models.DateField() #Data prazo

    def __str__(self):
        return f'{self.pat}, {self.munic}'