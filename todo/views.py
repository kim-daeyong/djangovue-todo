from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class TodoVueOnlyTV(TemplateView):
    template_name = 'todo/todo_vue_only.html'