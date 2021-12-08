from .models import TodoItem
from rest_framework import serializers
from datetime import datetime
from django.http import HttpResponseRedirect

class TodoItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoItem
        fields = ['id', 'content', 'create_time', 'finish_time']

'''
class TodoItemSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    content = serializers.CharField(required=True, allow_blank=False, max_length=100)
    create_time = serializers.DateTimeField(read_only=True)
    finish_time = serializers.DateTimeField(required=False, allow_null=True)
    
    def create(self, validated_data):
        return TodoItem.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.content = validated_data.get('content', instance.content)
        #instance.finish_time = datetime.now()
        instance.save()
        return instance
'''