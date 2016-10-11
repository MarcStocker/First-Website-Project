from django.shortcuts import render
from django.http import HttpResponse

from .models import TodoList

# Create your views here.
def index(request):
    todolist = TodoList.objects.all()
    context = {
        'page_name':"Home - EdgarRaw",
        'todolist': todolist,
    }
    return render(request, 'homepage.html', context)
