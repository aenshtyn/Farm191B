from django.db import models

# Create your models here.

class Owner(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
       return self.name
class Cow(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    age = models.PositiveIntegerField()
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name

    @classmethod
    def all_cows(cls):
        cows = Cow.objects.all()
        return cows



class Calf(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    age = models.CharField(max_length=255, blank=True, null=True)
    mother = models.ForeignKey(Cow, blank=True, null=True,on_delete=models.CASCADE)

    def __str__(self):
        return self.name



