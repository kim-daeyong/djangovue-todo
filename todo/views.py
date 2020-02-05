from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView, DeleteView

#template_name은 RedirecrView 이외에 모두 사
from todo.models import Todo


class TodoVueOnlyTV(TemplateView):
    template_name = 'todo/todo_vue_only.html'

#form 보여줘야하므로 모델, 필드 필요
class TodoCV(CreateView):
    model = Todo
    fields = '__all__'
    template_name = 'todo/todo_form.html'
    success_url = reverse_lazy('todo:list')

# 가져와야 하므로 model
class TodoLV(ListView):
    model = Todo
    template_name = 'todo/todo_list.html'

class TodoDelV(DeleteView):
    model = Todo
    template_name = 'todo/todo_confirm_delete.html'
    success_url = reverse_lazy('todo:list')