from django.db import models

# Create your models here.
class Cow(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    age = models.CharField(max_length=255, blank=True, null=True)
    owner = models.CharField(max_length=255, blank=True, null=True)


    def __str__(self):
        return self.name

    @classmethod
    def all_cows(cls):
        cows = Cow.object.all()
        return cows



class Calf(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    age = models.CharField(max_length=255, blank=True, null=True)
    mother = models.ForeignKey(Cow, blank=True, null=True,on_delete=models.CASCADE)

    def __str__(self):
        return self.name



