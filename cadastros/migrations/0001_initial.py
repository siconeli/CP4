# Generated by Django 4.2.4 on 2023-08-30 18:48

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
                ('pat', models.IntegerField(blank=True, unique=True, verbose_name='Processo N°')),
                ('municipio', models.CharField(blank=True, choices=[('selviria', 'Selvíria'), ('inocencia', 'Inocência')], max_length=50, verbose_name='Município')),
                ('uf', models.CharField(blank=True, choices=[('MS', 'MS'), ('MT', 'MT'), ('SP', 'SP'), ('RJ', 'RJ')], max_length=2, verbose_name='UF')),
                ('datini', models.DateField(blank=True, verbose_name='Data Inicial')),
                ('datfin', models.DateField(blank=True, verbose_name='Data Final')),
                ('datdivat', models.DateField(blank=True, verbose_name='Data Dívida Ativa')),
                ('valtrib', models.DecimalField(blank=True, decimal_places=2, max_digits=9, verbose_name='Valor do Atributo')),
                ('valmul', models.DecimalField(blank=True, decimal_places=2, max_digits=9, verbose_name='Valor da Multa')),
                ('valcred', models.DecimalField(blank=True, decimal_places=2, max_digits=9, verbose_name='Valor do Crédito')),
                ('valatu', models.DecimalField(blank=True, decimal_places=2, max_digits=9, verbose_name='Valor do Atualizado')),
                ('datvalatu', models.DateField(blank=True, verbose_name='Data Valor Atualizado')),
                ('datand', models.DateField(blank=True, verbose_name='Data Andamento')),
                ('datprazo', models.DateField(blank=True, verbose_name='Data Prazo')),
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
                ('Funcionario', models.CharField(max_length=50, verbose_name='Funcionário')),
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
