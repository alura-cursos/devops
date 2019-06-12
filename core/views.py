from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from .models import Todo
from .forms import TodoForm
from django.urls import reverse_lazy
from datetime import datetime


class TodoCreate(CreateView):
    model = Todo
    template_name = "core/new.html"
    form_class = TodoForm
    success_url = reverse_lazy('list_to_do')


class TodoList(ListView):
    model = Todo
    context_object_name = 'todos'
    template_name = 'core/index.html'

    def get_queryset(self):
        todo= Todo.objects.all().order_by('completed')
        return todo



def completed(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    todo.completed = True
    todo.completed_at = datetime.now()
    todo.save()
    return redirect('list_to_do')
