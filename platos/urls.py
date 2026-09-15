from django.urls import path
from . import views

app_name = 'platos'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('<int:id>/', views.detalle, name='detalle'),
]