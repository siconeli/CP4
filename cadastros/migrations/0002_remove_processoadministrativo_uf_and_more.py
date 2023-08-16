# Generated by Django 4.2.4 on 2023-08-15 20:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='processoadministrativo',
            name='uf',
        ),
        migrations.AlterField(
            model_name='processoadministrativo',
            name='anda',
            field=models.IntegerField(verbose_name='Andamento Atual'),
        ),
        migrations.AlterField(
            model_name='processoadministrativo',
            name='datand',
            field=models.DateField(verbose_name='Data Andamento'),
        ),
        migrations.AlterField(
            model_name='processoadministrativo',
            name='datdivat',
            field=models.DateField(verbose_name='Data D.A'),
        ),
        migrations.AlterField(
            model_name='processoadministrativo',
            name='datfin',
            field=models.DateField(verbose_name='Data Final'),
        ),
        migrations.AlterField(
            model_name='processoadministrativo',
            name='datini',
            field=models.DateField(verbose_name='Data Inicial'),
        ),
        migrations.AlterField(
            model_name='processoadministrativo',
            name='datprazo',
            field=models.DateField(verbose_name='Data Prazo'),
        ),
        migrations.AlterField(
            model_name='processoadministrativo',
            name='datvalatu',
            field=models.DateField(verbose_name='Data Valor Atualizado'),
        ),
        migrations.AlterField(
            model_name='processoadministrativo',
            name='valatu',
            field=models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Valor do Atualizado'),
        ),
        migrations.AlterField(
            model_name='processoadministrativo',
            name='valcred',
            field=models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Valor do Crédito'),
        ),
        migrations.AlterField(
            model_name='processoadministrativo',
            name='valmul',
            field=models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Valor da Multa'),
        ),
        migrations.AlterField(
            model_name='processoadministrativo',
            name='valtrib',
            field=models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Valor do Tributo'),
        ),
        migrations.CreateModel(
            name='UnidadeFederativa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uf', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cadastros.processoadministrativo')),
            ],
        ),
    ]
