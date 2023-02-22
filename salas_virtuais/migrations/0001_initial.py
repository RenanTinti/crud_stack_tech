# Generated by Django 4.1.7 on 2023-02-21 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sala',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.TextField(max_length=500)),
                ('categoria', models.CharField(choices=[('Programacao', 'Programação'), ('Design', 'Design'), ('Jogos_digitais', 'Jogos Digitais'), ('Mobile', 'Mobile')], max_length=100)),
                ('limite_participantes', models.IntegerField(default=50)),
                ('data_criacao', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
