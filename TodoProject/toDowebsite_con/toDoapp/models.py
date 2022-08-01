from pyexpat import model
from turtle import title, update
from venv import create
from django.db import models
from django.forms import DateField
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model): #id otomatik oluşuyor
    PRİORİTY = (
        ('string','low'),
        ('string','medium'),
        ('string','high'),
    )
    user = models.ForeignKey(User,null=True,blank=True, on_delete=models.CASCADE) 
    title = models.CharField(max_length=200,null=True,blank=True)
    description = models.TextField(null=True, blank=True)
    completed = models.BooleanField(default=False)
    start_date = models.DateField()
    end_date = models.DateField()
    priority = models.CharField( max_length=10, choices=PRİORİTY)

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['start_date']

  
