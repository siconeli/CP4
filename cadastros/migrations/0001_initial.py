# Generated by Django 4.2.4 on 2023-09-06 20:22

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
                ('municipio', models.CharField(choices=[('selviria', 'Selvíria'), ('inocencia', 'Inocência')], max_length=50, verbose_name='Município')),
                ('uf', models.CharField(choices=[('MS', 'MS'), ('MT', 'MT'), ('SP', 'SP'), ('RJ', 'RJ')], max_length=2)),
                ('datini', models.DateField(blank=True, null=True)),
                ('datfin', models.DateField(blank=True, null=True)),
                ('datdivat', models.DateField(blank=True, null=True)),
                ('valtrib', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('valmul', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True)),
                ('valcred', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True)),
                ('valatu', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True)),
                ('datvalatu', models.DateField(blank=True, null=True)),
                ('nomecontribuinte', models.CharField(max_length=50)),
                ('pessoa', models.CharField(choices=[('fisica', 'Física'), ('juridica', 'Jurídica')], max_length=50)),
                ('doc', models.CharField(max_length=14, unique=True, verbose_name='CPF/CNPJ')),
                ('nomefantasia', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.EmailField(blank=True, max_length=50, null=True)),
                ('logradouro', models.CharField(blank=True, max_length=50, null=True)),
                ('numero', models.IntegerField(blank=True, null=True)),
                ('complemento', models.CharField(blank=True, max_length=50, null=True)),
                ('bairro', models.CharField(blank=True, max_length=50, null=True)),
                ('municipiocontri', models.CharField(blank=True, choices=[('selviria', 'Selvíria'), ('inocencia', 'Inocência')], max_length=50, null=True)),
                ('ufcontri', models.CharField(blank=True, choices=[('MS', 'MS'), ('MT', 'MT'), ('SP', 'SP'), ('RJ', 'RJ')], max_length=2, null=True, verbose_name='UF')),
                ('cep', models.CharField(blank=True, max_length=10, null=True)),
                ('tel', models.CharField(blank=True, max_length=10, null=True)),
                ('cel', models.CharField(blank=True, max_length=10, null=True)),
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
                ('andamento', models.CharField(choices=[('abertura', 'Abertura'), ('fechamento', 'Fechamento')], max_length=50, verbose_name='Andamento')),
                ('dataprazo', models.DateField(verbose_name='Prazo')),
                ('locprocesso', models.CharField(max_length=50, verbose_name='Localização do Processo')),
                ('funcionario', models.CharField(max_length=50, verbose_name='Funcionário')),
                ('datrecebimento', models.DateField(verbose_name='Confirmado o Recebimento em')),
                ('complemento', models.CharField(max_length=150)),
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
