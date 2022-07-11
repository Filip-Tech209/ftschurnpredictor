from django.urls import path
from .import views


urlpatterns =[
#my views here

path('',views.index, name='index'),

path('predict/',views.predict, name='predict'),
path('churnRate',views.churnRate, name='churnRate'),
path('Causes',views.Causes, name='Causes'),
path('Measures',views.Measures, name='Measures'),
path('result',views.result, name='result'),
]