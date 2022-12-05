from django.db import models

# Create your models here.

class MyTodo(models.Model):
   task = models.CharField('задания'  , max_length=255)

   def __str__(self) -> str:
      return self.task