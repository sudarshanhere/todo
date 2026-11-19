from django.shortcuts import redirect, render, get_object_or_404
from .models import task 
from django.http import HttpResponseForbidden

# Create your views here.
def home(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        completed = request.POST.get('completed') == 'on'

        task.objects.create(title=title, description=description, completed=completed)

        return redirect('home')
        
    return render(request, 'home.html', {'tasks': task.objects.all()})

def update(request, task_id):
    task_obj = get_object_or_404(task, id=task_id)
    if request.method == 'POST':
        task_obj.title = request.POST.get('title')
        task_obj.description = request.POST.get('description')
        task_obj.completed = request.POST.get('completed') == 'on'
        task_obj.save()

        return redirect('home')
        
    return render(request, 'update.html', {'task': task_obj})

def delete(request, task_id):
    task_obj = get_object_or_404(task, id=task_id)
    if request.method == 'POST':
        task_obj.delete()

        return redirect('home')
        
    return render(request, 'delete.html', {'task': task_obj})