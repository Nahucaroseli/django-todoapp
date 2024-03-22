from django.http import JsonResponse
from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from todoapp.models import Task
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate,logout
# Create your views here.

def home(request):
   if request.user.is_authenticated:
        tasks = Task.objects.all()
        return render(request,'todoapp/home.html', {'tasks':tasks})
   else:
       return redirect('signup')



@csrf_exempt
def add_task(request):
    if request.method == 'POST':
            title = request.POST.get('title')
            user_id = request.user.id
            tarea = Task.objects.create(title=title,done=0,user_id=user_id)
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
    task.done = not task.done
    task.save()
    return redirect('Home')



def signup_view(request):
     return redirect('signup')
 
 
def signin_view(request):
    return redirect('signin')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('Home')  # Cambia 'task_list' por la vista de tu lista de tareas
    else:
        form = UserCreationForm()
    return render(request, 'todoapp/signup.html', {'form': form})



def signin(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirigir a la página de inicio o a la URL especificada en 'next'
                next_url = request.GET.get('next', 'Home')
                return redirect(next_url)
    else:
        form = AuthenticationForm()
    return render(request, 'todoapp/login.html', {'form': form})



def logout_view(request):
    logout(request)
    form = UserCreationForm()
    return redirect('signup')