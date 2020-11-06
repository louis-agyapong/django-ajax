from django.urls import path
from .views import person_create_view, load_cities, person_update_view

urlpatterns = [
    path("add/", person_create_view, name="person_add"),
    path('<int:pk>/', person_update_view, name='person_change'),
    path('load-cities/', load_cities, name='load_cities')
]