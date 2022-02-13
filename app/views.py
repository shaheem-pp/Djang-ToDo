from django.shortcuts import render, redirect

from app.models import *


# Create your views here.
def index(request):
    new_tasks = tbl_new_task.objects.all()
    return render(request, 'index.html',
                  {'title': 'ToDo | Index', 'new_tasks': new_tasks})


def add_task(request):
    null = ['', ' ', '   ', ',', '.']
    if request.POST.get('task') not in null:
        data = tbl_new_task()
        data.title = request.POST.get('task')
        data.status = "current"
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
    new_tasks.status = "completed"
    new_tasks.save()
    return redirect('/index')
