from django.shortcuts import render,redirect
from .models import todos
from .form import TodoForm

def home(request):
    todo=todos.objects.all()
    form =TodoForm()
    if request.method=="POST":
        form=TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    return render(request,"todo/home.html",{"todo":todo,"form":form})




def update(request,pk):
    todo=todos.objects.get(id=pk)
    form= TodoForm(instance=todo)
    if request.method=="POST":
        form=TodoForm(request.POST,instance=todo)
        if form.is_valid():
            form.save()
            return redirect("home")

    return render(request,"todo/update.html",{"todo":todo,"form":form})

def delete(request,pk):
    todo=todos.objects.get(id=pk)
    if request.method=="POST":
        todo.delete()
        return redirect ("home")
    return render(request,"todo/delete.html",{"todo":todo})