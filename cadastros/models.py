from django.db import models

from django.contrib.auth.models import User


class Base(models.Model): # Classe para registrar no banco de dados, data de criação e modificação dos registros.
    criados = models.DateField('Criação', auto_now_add=True)
    modificado = models.DateField('Atualização', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)
    
    class Meta:
        abstract = True


class ProcessoAdministrativo(Base): # Cadastro de processo administrativo - Campos do Formulário
    # Choices
    ufs = (
        ('MS', 'MS'), ('MT', 'MT'), ('SP', 'SP'), ('RJ', 'RJ'),
    )

    municipios = (
        ('selviria', 'Selvíria'), ('inocencia', 'Inocência'),
    )

    tipopessoa = (
        ('fisica', 'Física'), ('juridica', 'Jurídica'),
    )

    # Campos do processo administrativo
    pat = models.IntegerField(verbose_name='número', unique=True) # Número do processo
    municipio = models.CharField(max_length=50, choices=municipios) 
    uf = models.CharField(max_length=2, choices=ufs) 
    datini = models.DateField(blank=True, null=True) 
    datfin = models.DateField(blank=True, null=True)
    datdivat = models.DateField(blank=True, null=True)
    valtrib = models.DecimalField(decimal_places=2 , max_digits=9, blank=True, null=True) 
    valmul = models.DecimalField(decimal_places=2 , max_digits=9, blank=True, null=True) 
    valcred = models.DecimalField(decimal_places=2 , max_digits=9, blank=True, null=True)
    valatu = models.DecimalField(decimal_places=2 , max_digits=9, blank=True, null=True)
    datvalatu = models.DateField(blank=True, null=True) 
    datand = models.DateField(blank=True, null=True) 
    datprazo = models.DateField(blank=True, null=True)

    nomecontribuinte = models.CharField(max_length=50)  # Nome / Razão Social
    pessoa = models.CharField(max_length=50, choices=tipopessoa, blank=True, null=True) # Física / Jurídica
    doc = models.IntegerField(unique=True) # CPF / CNPJ
    nomefantasia = models.CharField(max_length=50, blank=True, null=True) # Nome Fantasia
    email = models.EmailField(max_length=50, blank=True, null=True) # E-mail
    logradouro = models.CharField(max_length=50, blank=True, null=True) # Rua
    numero = models.IntegerField(blank=True, null=True) # Número
    complemento = models.CharField(max_length=50, blank=True, null=True) # Complemento
    bairro = models.CharField(max_length=50, blank=True, null=True)
    municipiocontri = models.CharField(max_length=50, choices=municipios, blank=True, null=True) 
    ufcontri = models.CharField(max_length=2, choices=ufs, verbose_name='UF', blank=True, null=True) 
    cep = models.IntegerField(blank=True, null=True)
    tel = models.IntegerField(blank=True, null=True)
    cel = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f'{self.pat}'
    

class Andamento(Base): # Cadastro de andamentos - Campos do Formulário
    andamentos = (
        ('abertura', 'Abertura'), ('fechamento', 'Fechamento'),
    )

    processo = models.ForeignKey(ProcessoAdministrativo, on_delete=models.CASCADE) # Relacionamento 'One to Many'
    datandamento = models.DateField(verbose_name='Data do Andamento')
    andamento = models.CharField(max_length=50, choices=andamentos, verbose_name='Andamento')
    dataprazo = models.DateField(verbose_name='Prazo')
    locprocesso = models.CharField(max_length=50, verbose_name='Localização do Processo')
    funcionario = models.CharField(max_length=50, verbose_name='Funcionário')
    datrecebimento = models.DateField(verbose_name='Confirmado o Recebimento em')
    complemento = models.CharField(max_length=150)
    arq1 = models.FileField(upload_to='uploads/', verbose_name='Arquivo', blank=True) 
    arq2 = models.FileField(upload_to='uploads/', verbose_name='Arquivo', blank=True)
    arq3 = models.FileField(upload_to='uploads/', verbose_name='Arquivo', blank=True)
    arq4 = models.FileField(upload_to='uploads/', verbose_name='Arquivo', blank=True)
    arq5 = models.FileField(upload_to='uploads/', verbose_name='Arquivo', blank=True)
    arq6 = models.FileField(upload_to='uploads/', verbose_name='Arquivo', blank=True) # blank=True para remover a obrigatoriedade de preencher o campo. 

    def __str__(self):
        return f'Processo: {self.processo} Andamento: {self.andamento} Arquivo: {self.arq1} Arquivo: {self.arq2} Arquivo: {self.arq3} Arquivo: {self.arq4} Arquivo: {self.arq5} Arquivo: {self.arq6}'

