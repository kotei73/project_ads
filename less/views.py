from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

from .forms import UserForm



def index(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = UserForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            result = form.cleaned_data
            name = result['name']
            age = result['age']
            return HttpResponseNotFound('не найдено')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = UserForm()

    return render(request, 'index.html', {'form': form})
