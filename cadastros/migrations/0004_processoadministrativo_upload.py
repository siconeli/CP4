# Generated by Django 4.2.4 on 2023-08-24 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0003_remove_andamento_criador'),
    ]

    operations = [
        migrations.AddField(
            model_name='processoadministrativo',
            name='upload',
            field=models.FileField(default=1, upload_to='uploads/', verbose_name='Arquivo Processo'),
            preserve_default=False,
        ),
    ]
