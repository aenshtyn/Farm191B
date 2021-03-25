from django.db import models
from django.contrib.auth.models import User
# from utility.models import UserProfile,UserProfileBaseModel
# Create your models here.


class Employee(models.Model):
#   user              = models.OneToOneField(User, related_name="Employee",blank=True, null=True,on_delete=models.CASCADE)
    first_name= models.CharField(max_length=255, blank=True, null=True) 
    second_name= models.CharField(max_length=255, blank=True, null=True) 
    fathers_name= models.CharField(max_length=255, blank=True, null=True) 
    mothers_name= models.CharField(max_length=255, blank=True, null=True) 
    home_district= models.CharField(max_length=255, blank=True, null=True) 
    spouse_occupation= models.CharField(max_length=255, blank=True, null=True) 
    religion= models.CharField(max_length=255, blank=True, null=True) 
    date_joined= models.DateField( blank=True, null=True)
    entry_designation= models.CharField(max_length=255, blank=True, null=True) 
    entry_scale = models.CharField(max_length=255, blank=True, null=True) 
    picture = models.FileField(upload_to='documents/%Y/%m/%d',blank=True, null=True)     
    archive_status = models.CharField(max_length=32, choices=(('yes','yes'),('no','no')), blank=True) 
    status = models.CharField(max_length=32, choices=(('active','active'),('inactive','inactive')), blank=True) 

#   def get_full_name(self):
#         return self.user.first_name+" "+self.user.last_name
  
    def __str__(self):
          return self.first_name

    @classmethod
    def all_employees(cls):
        employees = Employee.objects.all()
        return employees
