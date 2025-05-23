# Generated by Django 5.1.7 on 2025-03-28 03:50

import django_cpf_cnpj.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='age',
        ),
        migrations.AddField(
            model_name='person',
            name='birthday_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='cpf',
            field=django_cpf_cnpj.fields.CPFField(blank=True, max_length=14, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='height',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='sex',
            field=models.CharField(blank=True, choices=[('m', 'M'), ('f', 'F')], null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='weight',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
