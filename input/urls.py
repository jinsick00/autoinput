from django.urls import path

from . import views

app_name = "input"

urlpatterns = [
    path('', views.input_index, name='index'),
    path("combine_files", views.combine_files, name="combine_files")
]