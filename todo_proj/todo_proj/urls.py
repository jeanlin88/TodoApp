"""todo_proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from todo.views import todo_View, addTodoView, editTodoView, finishTodoView, deleteTodoView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todo/', todo_View),
    path('addTodoItem/', addTodoView),
    path('editTodoItem/<int:i>/', editTodoView),
    path('finishTodoItem/<int:i>/', finishTodoView),
    path('deleteTodoItem/<int:i>/', deleteTodoView),
    path('', include('todo.urls'))
    #path('api/v1/todo/', include('todo.api_urls')),
    #path('api/v1/', include([
    #    path('todo/', include('todo.api_urls')),
    #])),
]