from django.db import models


class Base(models.Model): #Classe para registrar no banco de dados, data de criação e modificação dos registros.
    criados = models.DateField('Criação', auto_now_add=True)
    modificado = models.DateField('Atualização', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True

    
class UnidadeFederativa(Base):  #Não terá um formulário para cadastro, irei cadastrar todas as uf através do painel admin.
    uf = models.CharField(max_length=50) 

    def __str__(self):
        return f'{self.uf}'


class ProcessoAdministrativo(Base): #Cadastro de processo administrativo
    pat = models.IntegerField(verbose_name='PAT N°') #PAT n°
    munic = models.CharField(max_length=50, verbose_name='Município') #Município
    uf = models.ForeignKey(UnidadeFederativa, on_delete=models.PROTECT) # O 'PROTECT' protege na hora de um delete, não deixa excluir se possuir algum vínculo.
    datini = models.DateField(verbose_name='Data Inicial') #Data inicial
    datfin = models.DateField(verbose_name='Data Final') #Data final
    datdivat = models.DateField(verbose_name='Data Dívida Ativa') #Data dívida ativa
    valtrib = models.DecimalField(decimal_places=2 , max_digits=9, verbose_name='Valor do Atributo') #Valor do Tributo
    valmul = models.DecimalField(decimal_places=2 , max_digits=9, verbose_name='Valor da Multa') #Valor da Multa
    valcred = models.DecimalField(decimal_places=2 , max_digits=9, verbose_name='Valor do Crédito') #Valor do Crédito
    valatu = models.DecimalField(decimal_places=2 , max_digits=9, verbose_name='Valor do Atualizado') #Valor do Atualizado
    datvalatu = models.DateField(verbose_name='Data Valor Atualizado') #Data valor atualizado
    datand = models.DateField(verbose_name='Data Andamento') #Data andamento
    anda = models.IntegerField(verbose_name='Andamento Atual') #Andamento atual
    datprazo = models.DateField(verbose_name='Data Prazo') #Data prazo

    def __str__(self):
        return f'{self.pat}'