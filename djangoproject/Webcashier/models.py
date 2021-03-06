from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import datetime
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Employees(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    password = models.CharField(max_length=300, default='')
    first_name = models.CharField(max_length=300)
    last_name = models.CharField(max_length=300)
    dob = models.DateField(default = timezone.now)
    gen_der = models.CharField(max_length=300)
    age       = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.user.first_name}-{self.last_name}'
        
class Profile(models.Model):
    SUPERVISOR = 1
    EMPLOYEES = 2
    ROLE_CHOICES = (   
        (SUPERVISOR, 'Supervisor'), 
        (EMPLOYEES, 'Employees'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=30, blank=True)
    birthdate = models.DateField(null=True, blank=True)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, null=True, blank=True)

    def __str__(self):  # __unicode__ for Python 2
        return self.user.username

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        instance.profile.save()        

class Customer(models.Model):
    face_id    = models.IntegerField(primary_key=True)
    full_name  = models.CharField(max_length=300, default='')
    phone      = models.CharField(max_length=20, default='09999999999')
    gender     = models.CharField(max_length=300, default='ชาย')
    age        = models.CharField(max_length=20, default=20)
    email      = models.EmailField(null=True, unique=True, default='aaa@ubu.ac.th')

    def __str__(self):
        return f'{self.face_id} - {self.full_name}' 


class Incustumer(models.Model):
    face_id = models.IntegerField(primary_key=True) 
    first_name = models.CharField(max_length=300)
    last_name = models.CharField(max_length=300)
    phone = models.CharField(max_length=20)
    gender= models.CharField(max_length=300)
    age       = models.CharField(max_length=20)
    email = models.EmailField(null=True, unique=True)
    career = models.CharField(max_length=300)
    imageInfo = models.ImageField(upload_to='images/Incustumer/',null=True,blank=True)
    imageInfo2 = models.ImageField(upload_to='images/Incustumer/',null=True,blank=True)
    
    def __str__(self):
        return f'{self.face_id} - {self.first_name}  - {self.last_name}' 

class Order(models.Model):   
    Oid      = models.AutoField(primary_key=True)  
    Emp = models.OneToOneField(User, on_delete=models.CASCADE)
    user = models.OneToOneField(Incustumer, on_delete=models.CASCADE)
    list_Order  = models.CharField(max_length=300)
    sum_Order = models.CharField(max_length=300)   
    point = models.IntegerField()
    sum_price = models.IntegerField()
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    
    def __str__(self):
        return f'{self.Oid}-{self.Emp} '


class Product (models.Model):
    P_TYPE = (
        ('HOT', 'hot'),
        ('COLD', 'cold'),
        ('BLENDED', 'blended'),
    )

    Pid = models.AutoField(primary_key=True)
    P_name = models.CharField(max_length=1000)
    P_nameEng =models.CharField(max_length=1000)
    price = models.CharField(max_length=300)
    p_type =models.CharField(max_length=10,choices=P_TYPE, null=True, blank=True)
    created_at = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return f'{self.P_name} - {self.p_type }'

