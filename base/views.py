from django.shortcuts import render
from .models import Task
# listview 
from django.views.generic.list import ListView
# detail view
from django.views.generic.detail import DetailView
# create view
from django.views.generic.edit import CreateView
# update view
from django.views.generic.edit import UpdateView, DeleteView

from django.urls import reverse_lazy
"""
from django.http import HttpResponse
# Create your views here.
def tasklist(request):
    return HttpResponse('hello world')
"""    
# inherit Listview so  we have all functionalities that listview has
class TaskList(ListView):
    # used to display all the instances of table in signle view
    # Listview requires the model or queryset 
    # model is Task here 
    model = Task
    # by using context_object_name we can change the name of object 
    context_object_name = 'tasks'

class TaskDetail(DetailView):
    model = Task
    context_object_name = 'tasks'
    # by using template_name we can change the name of templte
    # for example here DetailView will look for the template file with prefix
    # detail so we have to create file with name task_detail.html but now we can 
    # change the file name
    template_name = 'base/task.html'
    fields = ['title', 'description', 'complete']

    #######
    




class CreateTask(CreateView):
    model = Task
    context_object_name = 'tasks'
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('tasks')

# udate task
class UpdateTask(UpdateView):
    model = Task
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('tasks')

# delete
class DeleteTask(DeleteView):
    model = Task
    context_object_name = 'tasks'
    success_url = reverse_lazy('tasks')



