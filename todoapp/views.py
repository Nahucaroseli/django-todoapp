from django.http import JsonResponse
from django.shortcuts import render,HttpResponse,redirect
from todoapp.models import Task
from django.views.decorators.csrf import csrf_exempt
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
            return redirect('todoapp/home.html')
    else:
        return JsonResponse({'status': 'error', 'message': 'Solicitud no válida'})


