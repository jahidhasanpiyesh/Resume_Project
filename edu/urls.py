from django.urls import path
from edu import views
urlpatterns = [
    path("educations/", views.skill, name="educations") 
]
