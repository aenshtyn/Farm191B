from django.db import models
from hr.models import Owner
# Create your models here.
class Cow(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    dob = models.DateField()
    age = models.PositiveIntegerField()
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, blank=True, null=True)
    purchase_date = models.DateField()
    breed = models.CharField(max_length=255, blank = True, null = True )

    def __str__(self):
        return self.name

    @classmethod
    def all_cows(cls):
        cows = Cow.objects.all()
        return cows

class MorningMilk(models.Model):
    cow = models.ForeignKey(Cow, blank=True, null=True,on_delete=models.CASCADE)
    date = models.DateField()
    volume = models.PositiveIntegerField()
 
    def __str__(self):
        return str(self.cow)


class AfternoonMilk(models.Model):
    cow = models.ForeignKey(Cow, blank=True, null=True,on_delete=models.CASCADE)
    date = models.DateField()
    volume = models.PositiveIntegerField()
 
    def __str__(self):
        return str(self.cow)

class EveningMilk(models.Model):
    cow = models.ForeignKey(Cow, blank=True, null=True,on_delete=models.CASCADE)
    date = models.DateField()
    volume = models.PositiveIntegerField()
 
    def __str__(self):
        return str(self.cow)
        
class DairyMeal(models.Model):
    bags_available = models.PositiveIntegerField()
    quantity_consumed = models.PositiveIntegerField()
    delivery_date = models.DateField()



class Calf(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    age = models.CharField(max_length=255, blank=True, null=True)
    mother = models.ForeignKey(Cow, blank=True, null=True,on_delete=models.CASCADE)

    def __str__(self):
        return self.name




