# Generated by Django 2.2.24 on 2021-10-24 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autenticacao', '0007_auto_20211024_1905'),
    ]

    operations = [
        migrations.AddField(
            model_name='imovel',
            name='disponivel',
            field=models.BooleanField(default=True),
        ),
    ]
