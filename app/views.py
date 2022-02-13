from django.shortcuts import render, redirect
from app.models import *


# Create your views here.
def index(request):
    new_tasks = tbl_new_task.objects.all()
    completed_tasks = tbl_completed_tasks.objects.all()
    return render(request, 'index.html',
                  {'title': 'ToDo | Index', 'new_tasks': new_tasks, 'completed_tasks': completed_tasks})


def add_task(request):
    null = ['', ' ', '   ', ',', '.']
    if request.POST.get('task') not in null:
        data = tbl_new_task()
        data.title = request.POST.get('task')
        data.save()
        return redirect('/index')
    else:
        return redirect('/index')


def remove_task(request, id):
    data = tbl_new_task.objects.get(id=id)
    data.delete()
    return redirect('/index')


def complete_task(request, id):
    new_tasks = tbl_new_task.objects.get(id=id)
    completed_tasks = tbl_completed_tasks.objects.all()
    completed_tasks.title = new_tasks.title
    new_tasks.save()
    completed_tasks.save()
    return redirect('/index')


def remove_completed_task(request, id):
    completed_tasks = tbl_completed_tasks.objects.get(id=id)
    completed_tasks.delete()
    return redirect('/index')
