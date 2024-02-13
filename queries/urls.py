

from django.urls import path
from . import views

urlpatterns = [
    path('query/', views.query_openai, name='query_openai'),
    path('add-data/', views.add_data, name='add_data'),
]