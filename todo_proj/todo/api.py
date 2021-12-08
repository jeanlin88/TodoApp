from django.views.decorators.csrf import csrf_exempt
from django.http.request import HttpRequest
from django.http.response import (
    HttpResponseNotFound,
    HttpResponseBadRequest,
    HttpResponse,
)
from .models import TodoItem
from json import dumps, loads, JSONEncoder
from datetime import datetime

"""
Create	[POST]	/api/v1/todo/items/
	201	Created：		資料新增成功
	400	Bad Request：	item為空
Read	[GET]	/api/v1/todo/items/
	200	Ok：			成功
Read	[GET]	/api/v1/todo/items/{id}
	200	Ok：			成功
	404	Not Found：		請求的資源不存在
Update	[PATCH]	/api/v1/todo/items/{id}
	200 Ok：        	請求成功，沒有返回內容
	400	Bad Request：	item為空
	404	Not Found：		請求的資源不存在
Delete	[DELETE] /api/v1/todo/items/{id}
	204 No Content：		請求成功，沒有返回內容
	404	Not Found：		請求的資源不存在
"""

class DateTimeEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime("%Y-%m-%d %H:%M:%S")
        else:
            return JSONEncoder.default(self, obj)

def create_content_item(item):
    item = {
        "id": item.id,
        "content": item.content,
        "create_time": item.create_time,
        "finish_time": item.finish_time,
    }
    return item

def Http2xx(status, res_msg=None, content=None):
    if (status == 200):
        return HttpResponse(
            status = status,
            content=dumps({"result": res_msg, "data": content}, cls=DateTimeEncoder),
        )
    else:
        return HttpResponse(status = status)

def Http400(err_msg, id):
    return HttpResponseBadRequest(content=dumps({"error": err_msg, "id": id}))

def Http404(err_msg, id):
    return HttpResponseNotFound(content=dumps({"error": err_msg, "id": id}))

@csrf_exempt
def todo_item_api(request, id=None):
    if id is None:
        if request.method == "GET":
            items = TodoItem.objects.all()
            content_items = []
            for item in items:
                content_items.append(create_content_item(item))
            if content_items:
                return Http2xx(200, "Items Found.", content_items)
            else:
                return Http2xx(200, "Items Found.", content_items)
        elif request.method == "POST":
            print('here')
            if request.body is None:
                return Http400("Item Content is Empty!", id)
            else:
                print(request.body)
                item = TodoItem(content=loads(request.body)["content"], create_time=datetime.now())
                item.save()
                return Http2xx(201)
    else:
        try:
            item = TodoItem.objects.get(id=id)
            if request.method == "GET":
                return Http2xx(200, "Items Found.", create_content_item(item))
            elif request.method == "PATCH":
                if request.body is None:
                    return Http400("Item Content is Empty!", id)
                else:
                    item.content = loads(request.body)["content"]
                    item.save()
                return Http2xx(204)
            elif request.method == "DELETE":
                item.delete()
                return Http2xx(204)
        except TodoItem.DoesNotExist:
            return Http404("Item Not Found!", id)
