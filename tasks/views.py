from django.shortcuts import get_object_or_404, render, redirect
from .models import Task
# Create your views here.
from .models import Task


def list_tasks(request):
    # Obtén las tareas pendientes y las terminadas por separado
    completed_tasks = Task.objects.filter(realizado=True)
    pending_tasks = Task.objects.filter(realizado=False)

    # Pasa las tareas completadas y las pendientes al template
    return render(request, 'list_tasks.html', {
        'completed_tasks': completed_tasks,
        'pending_tasks': pending_tasks,
    })
def create_task(request):
    task = Task(title = request.POST['title'], description=request.POST['description'])
    task.save()
    return redirect('/tasks/')

def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('/tasks/')



def update_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if request.method == 'POST':
        task.title = request.POST.get('title')
        task.description = request.POST.get('description')
        task.realizado = 'realizado' in request.POST
        task.save()
        return redirect('list_tasks')

    return render(request, 'update_task.html', {'task': task})
