from django.urls import path

from . import views

app_name = 'car_rental_app'
urlpatterns = [
    path('',views.home, name='home'),
    path('search/',views.search, name= 'search')
]