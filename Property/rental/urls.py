from django.urls import path
from . import views

urlpatterns = [
path('reserved_tables',views.reservations_table,name='reserved_tables'),
]