from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import GeeksModel
from .forms import GeeksForm


def create_view(request):
    context = {}
    form = GeeksForm()
    if request.method == 'POST':
        form = GeeksForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('geeks:create')
    context['form'] = form
    return render(request, 'geeks/form.html', context)


def list_view(request):
    context = {}
    geeks = GeeksModel.objects.all().order_by('-id')
    context['geeks'] = geeks
    return render(request, 'geeks/list.html', context)


def details_view(request, id):
    context = {}
    geek = get_object_or_404(GeeksModel, pk=id)
    context['geek'] = geek
    return render(request, 'geeks/details.html', context)


def update_view(request, id):
    context = {}
    geek = get_object_or_404(GeeksModel, pk=id)
    form = GeeksForm(instance=geek)
    if request.method == 'POST':
        form = GeeksForm(request.POST, instance=geek)
        if form.is_valid():
            form.save()
        url = reverse('geeks:details', args=(geek.id,))
        return redirect(url)
    context['form'] = form
    return render(request, 'geeks/form.html', context)


def delete_view(request, id):
    context = {}
    geek = get_object_or_404(GeeksModel, pk=id)
    if request.method == 'POST':
        geek.delete()
        return redirect('geeks:list')
    context['geek'] = geek
    return render(request, 'geeks/delete.html', context)
