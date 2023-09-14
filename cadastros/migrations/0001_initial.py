# Generated by Django 4.2.4 on 2023-09-14 17:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProcessoAdministrativo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criados', models.DateField(auto_now_add=True, verbose_name='Criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Atualização')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('pat', models.CharField(max_length=10, unique=True, verbose_name='N°')),
                ('municipio', models.CharField(choices=[('Selvíria', 'Selvíria'), ('Inocência', 'Inocência')], max_length=50, verbose_name='Município')),
                ('uf', models.CharField(choices=[('MS', 'MS'), ('MT', 'MT'), ('SP', 'SP'), ('RJ', 'RJ')], max_length=2)),
                ('datini', models.DateField(blank=True, null=True)),
                ('datfin', models.DateField(blank=True, null=True)),
                ('datdivat', models.DateField(blank=True, null=True)),
                ('valtrib', models.CharField(blank=True, max_length=14, null=True)),
                ('valmul', models.CharField(blank=True, max_length=14, null=True)),
                ('valcred', models.CharField(blank=True, max_length=14, null=True)),
                ('valatu', models.CharField(blank=True, max_length=14, null=True)),
                ('datvalatu', models.DateField(blank=True, null=True)),
                ('nomecontribuinte', models.CharField(max_length=50)),
                ('pessoa', models.CharField(choices=[('Física', 'Física'), ('Jurídica', 'Jurídica')], max_length=50)),
                ('doc', models.CharField(max_length=20, unique=True, verbose_name='CPF/CNPJ')),
                ('nomefantasia', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.EmailField(blank=True, max_length=50, null=True)),
                ('endereco', models.CharField(max_length=150)),
                ('complemento', models.CharField(blank=True, max_length=50, null=True)),
                ('municipiocontri', models.CharField(blank=True, choices=[('Selvíria', 'Selvíria'), ('Inocência', 'Inocência')], max_length=50, null=True)),
                ('ufcontri', models.CharField(blank=True, choices=[('MS', 'MS'), ('MT', 'MT'), ('SP', 'SP'), ('RJ', 'RJ')], max_length=2, null=True, verbose_name='UF')),
                ('cep', models.CharField(blank=True, max_length=10, null=True)),
                ('tel', models.CharField(blank=True, max_length=20, null=True)),
                ('cel', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Andamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criados', models.DateField(auto_now_add=True, verbose_name='Criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Atualização')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('datandamento', models.DateField(verbose_name='Data do Andamento')),
                ('andamento', models.CharField(choices=[('Abertura', 'Abertura'), ('Parecer Fiscal', 'Parecer Fiscal'), ('Decisão 1ª Instância', 'Decisão 1ª Instância'), ('Suspenso Para Fiscalização Futura', 'Suspenso Para Fiscalização Futura'), ('Auto de Infração e Termo de Intimação - AITI.', 'Auto de Infração e Termo de Intimação - AITI.'), ('Termo de Intimação Fiscal - TIF.-tif.', 'Termo de Intimação Fiscal - TIF.'), ('Decisão de 2ª Instância', 'Decisão de 2ª Instância'), ('Cobrança de Documentação', 'Cobrança de Documentação'), ('Recurso Voluntário', 'Recurso Voluntário'), ('Fim do Contrato com a Assessoria', 'Fim do Contrato com a Assessoria'), ('Manifestação', 'Manifestação'), ('Recebimento do AR', 'Recebimento do AR'), ('Despacho', 'Despacho'), ('Aguardando Pagamento', 'Aguardando Pagamento'), ('Apresentação de Documentação para Análise', 'Apresentação de Documentação para Análise'), ('Aguardando AR', 'Aguardando AR'), ('Ofício', 'Ofício'), ('Revelia', 'Revelia'), ('Execução', 'Execução'), ('Confissão de Dívida (Parcelamento)', 'Confissão de Dívida (Parcelamento)'), ('Reenvio de Documento', 'Reenvio de Documento'), ('Parecer Juridico', 'Parecer Juridico'), ('Certidão', 'Certidão'), ('Encaminhado', 'Encaminhado')], max_length=100, verbose_name='Andamento')),
                ('dias', models.IntegerField(blank=True, null=True)),
                ('dataprazo', models.DateField(blank=True, null=True)),
                ('funcionario', models.CharField(blank=True, max_length=50, null=True)),
                ('datrecebimento', models.DateField(blank=True, null=True)),
                ('complemento', models.CharField(blank=True, max_length=150, null=True)),
                ('arq1', models.FileField(blank=True, upload_to='uploads/', verbose_name='Arquivo')),
                ('arq2', models.FileField(blank=True, upload_to='uploads/', verbose_name='Arquivo')),
                ('arq3', models.FileField(blank=True, upload_to='uploads/', verbose_name='Arquivo')),
                ('arq4', models.FileField(blank=True, upload_to='uploads/', verbose_name='Arquivo')),
                ('arq5', models.FileField(blank=True, upload_to='uploads/', verbose_name='Arquivo')),
                ('arq6', models.FileField(blank=True, upload_to='uploads/', verbose_name='Arquivo')),
                ('processo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastros.processoadministrativo')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
