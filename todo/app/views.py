from django.shortcuts import render, redirect
from .models import *
from .forms import *
# Create your views here.


def home(request):
    apps = App.objects.all()
    form = appForm()

    if request.method == 'POST':
        form = appForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'apps': apps, 'form': form}

    return render(request, 'app/main.html', context)


def delete(request, pk):
    app = App.objects.get(id=pk)

    if request.method == 'POST':
        app.delete()
        return redirect('/')

    context = {'app': app}
    return render(request, 'app/delete.html', context)


def update(request, pk):
    app = App.objects.get(id=pk)

    form = appForm(instance=app)

    if request.method == 'POST':
        form = appForm(request.POST, instance=app)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}

    return render(request, 'app/update.html', context)

