from django.db import models
from django.contrib.auth import get_user_model

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
        ('Selvíria', 'Selvíria'), ('Inocência', 'Inocência'),
    )

    tipopessoa = (
        ('Física', 'Física'), ('Jurídica', 'Jurídica'),
    )

    # Campos do processo administrativo
    pat = models.CharField(unique=True, verbose_name='N°', max_length=10) # Número do processo
    municipio = models.CharField(max_length=50, choices=municipios, verbose_name='Município') # Município
    uf = models.CharField(max_length=2, choices=ufs) # UF 
    datini = models.DateField(blank=True, null=True) # Data Inicial do Período do processo
    datfin = models.DateField(blank=True, null=True) # Data final do Período do processo
    datdivat = models.DateField(blank=True, null=True) # Data dívida ativa
    valtrib = models.CharField(max_length=14, blank=True, null=True)  # Valor do atributo
    valmul = models.CharField(max_length=14, blank=True, null=True) # Valor da multa
    valcred = models.CharField(max_length=14, blank=True, null=True) # Valor do crédito
    valatu = models.CharField(max_length=14, blank=True, null=True) # Valor do atualizado
    datvalatu = models.DateField(blank=True, null=True) # Data valor atualizado
    nomecontribuinte = models.CharField(max_length=50)  # Nome / Razão Social
    pessoa = models.CharField(max_length=50, choices=tipopessoa) # Física / Jurídica
    doc = models.CharField(max_length=20, verbose_name='CPF/CNPJ', unique=True) # CPF / CNPJ
    nomefantasia = models.CharField(max_length=50, blank=True, null=True) # Nome Fantasia
    email = models.EmailField(max_length=50, blank=True, null=True) # E-mail
    endereco = models.CharField(max_length=150) # Rua
    # numero = models.IntegerField(blank=True, null=True) # Número 
    complemento = models.CharField(max_length=50, blank=True, null=True) # Complemento
    # bairro = models.CharField(max_length=50, blank=True, null=True) # Bairro
    municipiocontri = models.CharField(max_length=50, blank=True, null=True) # Município Contribuinte
    ufcontri = models.CharField(max_length=2, choices=ufs, verbose_name='UF', blank=True, null=True) # UF Contribuinte
    cep = models.CharField(max_length=10, blank=True, null=True) # CEP
    tel = models.CharField(max_length=20, blank=True, null=True) # Telefone
    cel = models.CharField(max_length=20, blank=True, null=True) # Celular

    def __str__(self):
        return f'{self.pat}'
    

class Andamento(Base): # Cadastro de andamentos - Campos do Formulário
    andamentos = (
        ('Abertura', 'Abertura'), ('Parecer Fiscal', 'Parecer Fiscal'), ('Decisão 1ª Instância', 'Decisão 1ª Instância'), ('Suspenso Para Fiscalização Futura', 'Suspenso Para Fiscalização Futura'), ('Auto de Infração e Termo de Intimação - AITI.', 'Auto de Infração e Termo de Intimação - AITI.'), ('Termo de Intimação Fiscal - TIF.-tif.', 'Termo de Intimação Fiscal - TIF.'), ('Decisão de 2ª Instância', 'Decisão de 2ª Instância'), ('Cobrança de Documentação', 'Cobrança de Documentação'), ('Recurso Voluntário', 'Recurso Voluntário'), ('Fim do Contrato com a Assessoria', 'Fim do Contrato com a Assessoria'), ('Manifestação', 'Manifestação'), ('Recebimento do AR', 'Recebimento do AR'), ('Despacho', 'Despacho'), ('Aguardando Pagamento', 'Aguardando Pagamento'), ('Apresentação de Documentação para Análise', 'Apresentação de Documentação para Análise'), ('Aguardando AR', 'Aguardando AR'), ('Ofício', 'Ofício'), ('Revelia', 'Revelia'), ('Execução', 'Execução'), ('Confissão de Dívida (Parcelamento)', 'Confissão de Dívida (Parcelamento)'), ('Reenvio de Documento', 'Reenvio de Documento'), ('Parecer Juridico', 'Parecer Juridico'), ('Certidão', 'Certidão'), ('Encaminhado', 'Encaminhado'),
    )
    
    # Campos do Andamento do processo administrativo
    processo = models.ForeignKey(ProcessoAdministrativo, on_delete=models.CASCADE) # Relacionamento 'One to Many'
    datandamento = models.DateField(verbose_name='Data do Andamento')
    andamento = models.CharField(max_length=100, choices=andamentos, verbose_name='Andamento')
    dias = models.IntegerField(blank=True, null=True)
    dataprazo = models.DateField(blank=True, null=True)
    # locprocesso = models.CharField(max_length=50, blank=True, null=True)
    funcionario = models.CharField(max_length=50, blank=True, null=True)
    datrecebimento = models.DateField(blank=True, null=True)
    complemento = models.CharField(max_length=150, blank=True, null=True)
    arq1 = models.FileField(upload_to='uploads/', verbose_name='Arquivo', blank=True) 
    arq2 = models.FileField(upload_to='uploads/', verbose_name='Arquivo', blank=True)
    arq3 = models.FileField(upload_to='uploads/', verbose_name='Arquivo', blank=True)
    # arq4 = models.FileField(upload_to='uploads/', verbose_name='Arquivo', blank=True)
    # arq5 = models.FileField(upload_to='uploads/', verbose_name='Arquivo', blank=True)
    # arq6 = models.FileField(upload_to='uploads/', verbose_name='Arquivo', blank=True) # blank=True para remover a obrigatoriedade de preencher o campo. 

    def __str__(self):
        return f'Processo: {self.processo} Andamento: {self.andamento} Arquivo: {self.arq1} Arquivo: {self.arq2} Arquivo: {self.arq3}'

