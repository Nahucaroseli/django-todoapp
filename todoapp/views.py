from django.http import JsonResponse
from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from todoapp.models import Task
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
# Create your views here.


def home(request):
    tasks = Task.objects.all()
    return render(request,'todoapp/home.html', {'tasks':tasks})




@csrf_exempt
def add_task(request):
    if request.method == 'POST':
            title = request.POST.get('title')
            tarea = Task.objects.create(title=title,done=0)
            tarea.save()
            return redirect('Home')
    else:
        return JsonResponse({'status': 'error', 'message': 'Solicitud no válida'})
    
    
    
    


@csrf_exempt
def delete_task(request):
    task_id = request.POST.get('task_id')
    task = get_object_or_404(Task, taskId=task_id)
    task.delete()
    return redirect('Home')





@csrf_exempt
def modify_task(request):
    task_id = request.POST.get('task_id')
    task = get_object_or_404(Task, taskId=task_id)
    if task.done == False:
        task.done = True
    else:
        task.done = False
    task.save()
    return redirect('Home')