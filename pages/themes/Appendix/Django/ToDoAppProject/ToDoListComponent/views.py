from django.shortcuts import render
from django.http import HttpResponse
from .models import Task

def index(request):

    task_list = Task.objects.all()

    return render(
        request,
        'tasks_index.html',
        {
            'task_list' : task_list,
        }
    )