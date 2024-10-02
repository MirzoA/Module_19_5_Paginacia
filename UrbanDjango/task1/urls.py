from django.urls import path
from . import views


urlpatterns = [
    path('1/', views.index1, name = 'index1'),
    path('2/', views.listing, name = 'index2'),

]
