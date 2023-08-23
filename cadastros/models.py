from django.db import models


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

    pat = models.IntegerField(verbose_name='PAT N°', unique=True, help_text='Número real do processo.') # Número do processo
    municipio = models.CharField(max_length=50, choices=municipios, verbose_name='Município') 
    uf = models.CharField(max_length=2, choices=ufs, verbose_name='UF') 
    datini = models.DateField(verbose_name='Data Inicial') 
    datfin = models.DateField(verbose_name='Data Final')
    datdivat = models.DateField(verbose_name='Data Dívida Ativa')
    valtrib = models.DecimalField(decimal_places=2 , max_digits=9, verbose_name='Valor do Atributo') 
    valmul = models.DecimalField(decimal_places=2 , max_digits=9, verbose_name='Valor da Multa') 
    valcred = models.DecimalField(decimal_places=2 , max_digits=9, verbose_name='Valor do Crédito')
    valatu = models.DecimalField(decimal_places=2 , max_digits=9, verbose_name='Valor do Atualizado')
    datvalatu = models.DateField(verbose_name='Data Valor Atualizado') 
    datand = models.DateField(verbose_name='Data Andamento') 
    datprazo = models.DateField(verbose_name='Data Prazo')
    #upload = models.FileField(upload_to='uploads/', verbose_name='Arquivo Processo')  # Para fazer upload de arquivos


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
    Funcionario = models.CharField(max_length=50, verbose_name='Funcionário')
    datrecebimento = models.DateField(verbose_name='Confirmado o Recebimento em')
    complemento = models.CharField(max_length=150)

    def __str__(self):
        return f'{self.processo} {self.andamento}'





    