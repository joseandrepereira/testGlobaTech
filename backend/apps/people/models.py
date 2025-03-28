from django_cpf_cnpj.fields import CPFField
from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False)

    birthday_date = models.DateField(blank=True, null=True)

    cpf = CPFField(max_length=14, blank=True, null=True)

    sex_choices = (
        ('m', 'M'),
        ('f', 'F')
    )
    sex = models.CharField(choices=sex_choices, null=True, blank=True)

    height = models.DecimalField(decimal_places=2, max_digits=10, null=True, blank=True)

    weight = models.DecimalField(decimal_places=2, max_digits=10, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name