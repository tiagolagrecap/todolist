from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm


def index(request):
    tasks = Task.objects.all()
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'tasks': tasks, 'form': form}
    return render(request, 'todolist/index.html', context)


def update_task(request, pk):
    item = Task.objects.get(id=pk)
    form = TaskForm(instance=item)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'item': item, 'form': form}
    return render(request, 'todolist/update_task.html', context)


def delete_task(request, pk):
    item = Task.objects.get(id=pk)
    item.delete()
    return redirect('/')


def done(request, pk):
    name = Task.objects.get(id=pk)
    name.completed = True
    name.save()
    return redirect('/')


def undone(request, pk):
    name = Task.objects.get(id=pk)
    name.completed = False
    name.save()
    return redirect('/')
