from django.core.checks import messages
from django.http.response import HttpResponseBadRequest, HttpResponseNotFound
from django.shortcuts import render
#from .models import TodoItem
from django.http import HttpResponseRedirect
import datetime
from itertools import chain
#from .serializers import TodoItemSerializer

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from todo.models import TodoItem
from todo.serializers import TodoItemSerializer
from json import dumps

@csrf_exempt
@api_view(['GET', 'POST'])
def Todo_List(request):
    # Read all items
    if request.method == "GET":
        todo_items = TodoItem.objects.filter(finish_time=None).order_by("id")
        finished_items = (
            TodoItem.objects.all().exclude(finish_time=None).order_by("finish_time")
        )
        all_todo_items = list(chain(todo_items, finished_items))
        serializer = TodoItemSerializer(all_todo_items, many=True)
        return JsonResponse(serializer.data, safe=False)
    # Create new item
    elif request.method == "POST":
        serializer = TodoItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        #return HttpResponseBadRequest(content=dumps({"error": f"Create item failed! {serializer.errors}"}))
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
@api_view(['GET', 'PATCH', 'DELETE'])
def Todo_Detail(request, item_id):
    #check if item exist
    try:
        item = TodoItem.objects.get(id=item_id)
    except TodoItem.DoesNotExist:
        return HttpResponseNotFound(
            content=dumps({"error": "Item Not Found!", "id": item_id})
        )
    # Read item
    if request.method == "GET":
        serializer = TodoItemSerializer(item)
        return JsonResponse(serializer.data)
    # Update item
    elif request.method == "PATCH":
        serializer = TodoItemSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    # Delete item
    elif request.method == "DELETE":
        item.delete()
        return HttpResponse(status=204)

# Create your views here.
def todo_View(request):
    todo_items = TodoItem.objects.filter(finish_time=None).order_by("id")
    finished_items = (
        TodoItem.objects.all().exclude(finish_time=None).order_by("finish_time")
    )
    all_todo_items = list(chain(todo_items, finished_items))
    return render(request, "todo_list.html", {"all_items": all_todo_items})


def addTodoView(request):
    thing = request.POST.get("content", True)
    new_item = TodoItem(content=thing)
    new_item.save()
    return HttpResponseRedirect("/todo/")


def editTodoView(request, i):
    thing = request.POST.get("new_todo", True)
    item = TodoItem.objects.get(id=i)
    item.content = thing
    item.save()
    return HttpResponseRedirect("/todo/")


def finishTodoView(request, i):
    finish_item = TodoItem.objects.get(id=i)
    finish_item.finish_time = datetime.datetime.now()
    finish_item.save()
    return HttpResponseRedirect("/todo/")


def deleteTodoView(reuqest, i):
    y = TodoItem.objects.get(id=i)
    y.delete()
    return HttpResponseRedirect("/todo/")
