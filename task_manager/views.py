from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

# Create your views here.

def home(request):
    if request.method == 'POST':
        form = TaskForm(request.POST or None)
        if form.is_valid():
            form.save()
            all_tasks = Task.objects.filter(done=False)
            return render(request, 'home.html', {'all_tasks': all_tasks})
        else:
             return redirect('home')
    else:
        all_tasks = Task.objects.filter(done=False)
        return render(request, 'home.html', {'all_tasks': all_tasks})


def completed(request):
    if request.method=='GET':
        done_tasks = Task.objects.filter(done=True)

        return render(request, 'completed.html', {'done_tasks': done_tasks})


def deleteTask(request, task_id):
        task = Task.objects.get(id=task_id)
        task.delete()
        return redirect('home')


def changeStatusTrue(request, task_id):
     task = Task.objects.get(id = task_id)
     task.done = True
     task.save()
     return redirect('home')

def changeStatusFalse(request, task_id):
     task = Task.objects.get(id = task_id)
     task.done = False
     task.save()
     return redirect('completed')
     

def editTask(request, id):
    if request.method == 'POST':
        data = Task.objects.get(pk=id)
        form = TaskForm(request.POST or None, instance=data)
            
        if form.is_valid():
            form.save()
    else:
        data = Task.objects.get(pk=id)
        return render(request, 'edit.html', {'data':data})
    return redirect('home')