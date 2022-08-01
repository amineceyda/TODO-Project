from django.urls import path

from . import views
from .views import ListTask


urlpatterns = [
   path('', ListTask.as_view(), name='listTask'),
    

]