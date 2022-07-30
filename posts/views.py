from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from .forms import Todo_listForm
from django.core import serializers
from django.http import JsonResponse
from .models import Todo_list

# Create your views here.

def home(request):
    if request.method == 'POST':

        todo_list = Todo_list()
        todo_list.title = request.POST['name']
        todo_list.save()

    todo_list = Todo_list.objects.all().order_by('-id')
    content = {
        'todo': todo_list
    }
    return render(request, 'home.html', content)

def edit(request, **kwargs):
    id = kwargs.get('slug')
    if request.method == 'POST':
        task = Todo_list.objects.get(id=id)
        task.title = request.POST.get('title')
        task.description = request.POST.get('description')
        task.status = request.POST.get('status')
        task.save()

        return redirect('home')
    else:
        todo = Todo_list.objects.get(id=id)
        context = {
            'todo':todo
        }
        return render(request, 'todo-edit.html', context);

def delete(request, **kwargs):
    id = kwargs['slug']
    todo = Todo_list.objects.get(id=id)
    todo.delete()
    return redirect('home')

def common(request, **kwargs):
    path = kwargs.get('path')
    if(path == 'news'):
        return HttpResponse("this is common url")
    else:
        raise Http404
