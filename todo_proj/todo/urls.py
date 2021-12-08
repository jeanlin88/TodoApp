from django.urls import path
from todo.views import Todo_Detail,Todo_List

urlpatterns = [
    path('api/v1/todo/items/', Todo_List),
    path('api/v1/todo/items/<int:item_id>/', Todo_Detail),
]