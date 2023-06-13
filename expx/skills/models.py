from django.db import models
from django.core.validators import MaxValueValidator
# Create your models here.

skillType = (
    ("Normal","Normal"),
    ("Verified","Verified"),
    ("Premium","Premium")
)
dayType = (
    ("Lesson","Lesson"),
    ("Practice","Practice"),
    ("Rest","Rest")
)
skillStatus=(
    ("Draft","Draft"),
    ("Published","Published"),
)
class SkillModel(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    icon = models.ImageField()
    creator = models.CharField(max_length=50)
    
    description = models.TextField(max_length=500)
    price = models.PositiveIntegerField(validators=MaxValueValidator(99999))
    type = models.CharField(max_length=10, choices=skillType, default="Normal")
    downloads = models.IntegerField()
    published_status = models.CharField(max_length=10, choices=skillStatus)
    
class ReviewModel(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.CharField(max_length=50)
    content = models.TextField(max_length=1000)
    rating = models.IntegerField(validators=MaxValueValidator(5))
    posted_day = models.DateField(auto_now_add=True)
    
class DayModel(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    type =models.CharField(choices=dayType)
    content = models.TextField(max_length=10000)