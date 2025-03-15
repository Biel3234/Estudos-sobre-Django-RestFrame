from django.urls import path
from .views import *

app_name = 'app'

urlpatterns = [
    path('teste/', create_list, name='criar'),
    path('teste/<int:pk>/', detail_delete_edit, name='editar')
]