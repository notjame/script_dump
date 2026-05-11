from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotAllowed
from .forms import PersonForm, TodoForm
from .models import Todo

# Create your views here.
def hello_world_view(request):
    return HttpResponse('Hello World')

def hello_python_view(request):
    return HttpResponse('Hello Python')

def hello_html_view(request):
    return render(request, 'todos/hello.html')

def hello_path(request, num1, num2):
    return HttpResponse(f'Sum is {num1 + num2}!') 

def hello_query(request):
    return HttpResponse(f'Your query was {request.GET.get("q")}')

def special_view(request):
    #do some stuff

    return redirect('hello_html')

def post_example(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            age = form.cleaned_data['age']
            job = form.cleaned_data['job']

        return HttpResponse(f'You posted: {name}, {age}, {job}')
    else: 
        return HttpResponseNotAllowed(['POST'])

def submit_example(request):
    return render(request, 'todos/submit.html')

def submit_django_form(request):
    form = PersonForm()
    return render(request, 'todos/submit_django_form.html', {'form': form})

def template_view(request):
    context = {
        "name": "Mike",
        "age": 30,
        "skills": ["Python", "SQL"]
    }
    return render(request, 'todos/template_demo.html', context)

def todos_view(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save()
            return HttpResponse('ToDo successfully created!')
    else:
        form = TodoForm()
        todos = Todo.objects.all()

        return render(request, 'todos/todos.html', {'form': form, 'todos': todos})

