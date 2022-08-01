from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.generic.list import ListView
from .models import Task

class ListTask(ListView):
    model = Task
    
