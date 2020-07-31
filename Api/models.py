from django.db import models

# Create your models here.


class Owner(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=100)
    contactNo = models.IntegerField(default=9999999999)
    vaddo = models.CharField(max_length=100)


class Buisness(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    houseNo = models.CharField(max_length=100, primary_key=True)
    establishmentName = models.CharField(max_length=150)
    rooms = models.IntegerField(default=1)
    type = models.CharField(max_length=50)
    vaddo = models.CharField(max_length=150)


class Taxes(models.Model):
    buisness = models.ForeignKey(Buisness, on_delete=models.CASCADE)
    tradeTax = models.IntegerField(default=0)
    boardTax = models.IntegerField(default=0)
    garbageTax = models.IntegerField(default=0)
    startDate = models.DateField()
    dueDate = models.DateField()
    Year = models.IntegerField()


class Application(models.Model):
    buisness = models.ForeignKey(Buisness, on_delete=models.CASCADE)
    applicationNo = models.IntegerField(primary_key=True)
    applicationDate = models.DateField()
    resolutionNo = models.CharField(max_length=50)
    resolutionDate = models.DateField()
    sarpanchRemark = models.CharField(max_length=300)
