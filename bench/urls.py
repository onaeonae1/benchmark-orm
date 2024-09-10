from django.urls import path
from app import views

urlpatterns = [
    path("raw_api/", views.raw_sql_api),
    path("orm_api/", views.orm_api),
]
