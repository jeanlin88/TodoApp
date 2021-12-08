from django.urls import path
from . import api

app_name = "todo_item_api"

urlpatterns = [
    path('items/', api.todo_item_api),
    path('items/<int:id>', api.todo_item_api),
]
