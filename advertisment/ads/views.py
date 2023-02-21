from django.shortcuts import render, redirect
from .models import Ads, Rubric
from django.views.generic.edit import CreateView
from ads.forms import AdsForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
def index(request):  # контроллер-функция, выводит главную страницу
    ads = Ads.objects.order_by('-published')
    rubrics = Rubric.objects.all()
    return render(request, 'ads/index.html',
                  {'ads': ads, 'rubrics': rubrics})  # в контекст передаются все рубрики и объявления по дате публикации


def by_rubric(request, rubric_id):  # контроллер-функция, вывод объявлений по рубрикам
    ads = Ads.objects.filter(rubric=rubric_id)
    rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.get(id=rubric_id)
    context = {'ads': ads, 'rubrics': rubrics, 'current_rubric': current_rubric}
    return render(request, 'ads/by_rubric.html', context)


class AdsCreateView(CreateView):
    template_name = 'ads/create.html'
    form_class = AdsForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context


def register(request):
    form = UserCreationForm()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('/ads/')
    return render(request, 'ads/register.html', {'form': form})
