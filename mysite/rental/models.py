from django.db import models

# Create your models here.

class House_address(models.Model):
    house_number = models.CharField(max_length=50)
    village = models.CharField(max_length=100)
    subdistrict = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

class Rent_rate(models.Model):
    mouth_rate = models.IntegerField(default=0)
    electric_rate = models.IntegerField(default=0)
    water_rate = models.IntegerField(default=0)

class House(models.Model):
    house_name = models.CharField(max_length=100)
    house_address_id = models.ForeignKey(House_address, on_delete=models.CASCADE)
    rent_rate_id = models.ForeignKey(Rent_rate, on_delete=models.CASCADE)