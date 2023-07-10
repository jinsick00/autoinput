from django.urls import path

from . import views

app_name = "board"

urlpatterns = [
    path('', views.board_index, name='index'),
    path('<int:post_id>', views.board_detail, name='detail'),
    path('write', views.board_write, name='write'),

]