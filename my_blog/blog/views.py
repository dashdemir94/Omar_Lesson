from django.shortcuts import render
from django.http import HttpResponse
from .models import Task
# Create your views here.
def task_list(request):
    tasks = Task.objects.all().order_by('date')
    return render(request,'blog/post_list.html', {'tasks': tasks})