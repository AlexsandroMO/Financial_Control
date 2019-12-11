from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Task
from .forms import TaskForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
import main
import pandas as pd
import datetime


@login_required
def taskList(request):

    user = request.user
    ss = main.read_sql_user_name(user)
    id_user = ss.username[0]

    search = request.GET.get('search')
    filtery = request.GET.get('filtery')
    taskDoneRecently = Task.objects.filter(done='pago', update_at__gt=datetime.datetime.now()-datetime.timedelta(days=30), user=request.user).count()
    taskPago = Task.objects.filter(done='pago', user=request.user).count()
    taskPagar = Task.objects.filter(done='pagar', user=request.user).count()

    if search:
        tasks = Task.objects.filter(name__icontains=search, user=request.user)
    elif filtery:
        tasks = Task.objects.filter(done=filtery, user=request.user)
    else:
        tasks_list = Task.objects.all().order_by('-type_task').filter(user=request.user)
        paginator = Paginator(tasks_list, 8) #quantidde de linhas
        page = request.GET.get('page')
        tasks = paginator.get_page(page)


    return render(request, 'conta/list.html', {'tasks': tasks, 'id_user': id_user,
                            'taskDoneRecently': taskDoneRecently, 'taskPago': taskPago, 'taskPagar': taskPagar})

@login_required
def taskView(request, id):
    task = get_object_or_404(Task, pk=id)
    return render(request, 'conta/task.html', {'task': task})


@login_required
def newTask(request):

    if request.method == 'POST':
        form = TaskForm(request.POST)

        if form.is_valid():
            task = form.save(commit=False)
            task.done = 'Pagar'
            task.user = request.user
            task.save()

            return redirect('/')

    else:
        form = TaskForm()
        return render(request, 'conta/addtask.html', {'form': form})

@login_required
def editTask(request, id):
    #task = Task.objects.create(description ="GfG is the best")
    #task.save()

    task = get_object_or_404(Task, pk=id)
    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)

        if form.is_valid():
            task.save()
            return redirect('/')
        else:
            return render(request, 'conta/edittask.html', {'form': form, 'task': task})

    else:
        return render(request, 'conta/edittask.html', {'form': form, 'task': task})



@login_required
def deleteTask(request, id):
    task = get_object_or_404(Task, pk=id)
    task.delete()

    messages.info(request, 'Tarefa deletada com sucesso.')
    return redirect('/')



@login_required
def changeStatus(request, id):
    task = get_object_or_404(Task, pk=id)

    if (task.done == 'Pagar'):
        task.done = 'Pago'
    else:
        task.done = 'Pagar'
    
    task.save()

    return redirect('/')


@login_required
def faturaTask(request):

    aa = main.read_sql_xx()
    ss = main.read_sql_user(request.user)

    id_user = ss.id[0]

    df = main.read_sql(id_user)
    df2 = main.read_sql2(id_user)
    x = df.varcont
    y = df2.varcont

    new = []
    for a in x:
        new.append(a)

    dd = pd.DataFrame(data=new,columns=['Calc'])
    faturar_x = dd['Calc'].sum()

    new2 = []
    for a in y:
        new2.append(a)

    dd = pd.DataFrame(data=new2,columns=['Calc'])
    faturar_y = round(float(dd['Calc'].sum()),2)

    faturamento = faturar_y + faturar_x


    return render(request, 'conta/fatura.html', {'faturar_x': faturar_x,'faturar_y': faturar_y,'faturamento': faturamento})






#Testes
def yourName(request):
    nome = 'ok'
    return render(request, 'conta/list.html', {'nome': nome})


def helloworld(request):
    return HttpResponse('Hello World!')




