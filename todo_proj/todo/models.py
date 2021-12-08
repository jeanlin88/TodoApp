from django.db import models

# Create your models here.
class TodoItem(models.Model):
    content = models.TextField(blank=False)
    create_time = models.DateTimeField(auto_now_add=True)
    finish_time = models.DateTimeField(null=True)
    class Meta:
        ordering = ['create_time']