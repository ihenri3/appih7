# Generated by Django 4.0.1 on 2022-01-04 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=50)),
                ('telefone', models.CharField(max_length=20)),
                ('endereco', models.CharField(max_length=70)),
                ('bairro', models.CharField(max_length=30)),
                ('cidade', models.CharField(max_length=30)),
                ('cep', models.IntegerField()),
            ],
        ),
    ]
