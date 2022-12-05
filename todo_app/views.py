from django.shortcuts import render , redirect
from .models import MyTodo
from .forms import TodoForm
# Create your views here.

def alltodos(request):
   tasks = MyTodo.objects.all()
   form = TodoForm()
   if request.method == 'POST':
      form = TodoForm(request.POST)
      if form.is_valid():
         form.save()
   context = {
      'tasks':tasks,
      'form':form
   }
   return render(request , 'alltodo.html' , context)

def deleteTodo(request , pk):
   task = MyTodo.objects.get(id=pk)
   task.delete()
   return redirect('/')

def updateTodo(request , pk):
   todo = MyTodo.objects.get(id=pk)
   print(todo)
   updateForm = TodoForm(instance=todo)
   if request.method == 'POST':
      updateForm = TodoForm(request.POST , instance=todo)
      if updateForm.is_valid():
         updateForm.save()
         return redirect('/')
   context = {
      'todo' : todo,
      'update': updateForm
   }
   return render(request , 'updateEL.html' , context )