# Generated by Django 2.2.24 on 2021-10-23 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('cpf', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=100)),
                ('telefone', models.CharField(max_length=100)),
            ],
        ),
    ]
