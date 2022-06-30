from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Client(models.Model):

    name = models.CharField('name', max_length=256, unique=True)

    def __str__(self):
        return self.name


class Organization(models.Model):

    client_name = models.ForeignKey(Client, verbose_name='client_name', on_delete=models.CASCADE)
    name = models.CharField('name', max_length=256)
    address = models.CharField('address', max_length=256)
    fraud_weight = models.IntegerField('fraud_weight', null=True, blank=True)

    class Meta:
        unique_together = ('client_name', 'name',)

    def __str__(self):
        return f"{self.client_name} {self.name}"


class Bill(models.Model):
    client_name = models.ForeignKey(Client, verbose_name='client_name', on_delete=models.CASCADE)
    client_org = models.ForeignKey(Organization, verbose_name='client_org', on_delete=models.CASCADE)
    number = models.IntegerField('number')
    summary = models.FloatField('summary')
    date = models.DateField('date')
    service = models.CharField('service', max_length=256)
    fraud_score = models.FloatField('fraud score', null=True, blank=True)
    service_class = models.IntegerField('service class', null=True, blank=True)
    service_name = models.CharField('service name', max_length=256, null=True, blank=True)

    class Meta:
        unique_together = ('client_org', 'number',)

    def __str__(self):
        return f"{self.client_org} {self.number}"
