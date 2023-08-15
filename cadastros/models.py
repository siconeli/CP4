from django.db import models

class ProcessoAdministrativo(models.Model):
    pat = models.IntegerField(verbose_name='PAT N°') #PAT n°
    munic = models.CharField(max_length=50, verbose_name='Município') #Município
    uf = models.CharField(max_length=2) 
    datini = models.DateField(verbose_name='Data Inicial') #Data inicial
    datfin = models.DateField(verbose_name='Data Final') #Data final
    datdivat = models.DateField(verbose_name='Data D.A') #Data dívida ativa
    valtrib = models.DecimalField(decimal_places=2 , max_digits=9, verbose_name='Valor do Tributo') #Valor do Tributo
    valmul = models.DecimalField(decimal_places=2 , max_digits=9, verbose_name='Valor da Multa') #Valor da Multa
    valcred = models.DecimalField(decimal_places=2 , max_digits=9, verbose_name='Valor do Crédito') #Valor do Crédito
    valatu = models.DecimalField(decimal_places=2 , max_digits=9, verbose_name='Valor do Atualizado') #Valor do Atualizado
    datvalatu = models.DateField(verbose_name='Data Valor Atualizado') #Data valor atualizado
    datand = models.DateField(verbose_name='Data Andamento') #Data andamento
    anda = models.IntegerField(verbose_name='Andamento Atual') #Andamento atual
    datprazo = models.DateField(verbose_name='Data Prazo') #Data prazo
    
    def __str__(self):
        return str(self.pat), self.munic
    
class uf

