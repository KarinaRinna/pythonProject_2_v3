from django.shortcuts import render, redirect
from .models import Artiles
from .forms import ArtilesForm
from django.views.generic import DetailView, UpdateView, DeleteView


def news_home(request):
    news = Artiles.objects.order_by('-date') #Сортируем по дате публикации
    return render(request, 'news/news_home.html', {'news': news})


class NewsDetailView(DetailView):
    model = Artiles
    template_name = 'news/details_view.html'
    context_object_name = 'artile'


class NewsUpdateView(UpdateView):
    model = Artiles
    template_name = 'news/create.html'

    form_class = ArtilesForm


class NewsDeleteView(DeleteView):
    model = Artiles
    success_url = '/news/'          #тут после удаления переадресовываем на невс
    template_name = 'news/news-delete.html'


def create(request):
    error = ''
    if request.method == 'POST':    # если нажму добавить статью то выполнится проверка
        form = ArtilesForm(request.POST) # получаем все данные что ввел пользователь
        if form.is_valid():     #Являются ли данные корректно заполненные
            form.save()       # Тогда сохраняем запись
            return redirect('news_home') # и после сохранения переадресуемся на новостную страницу
        else:   # Если некорректно заполнены
            error = 'Форма была неверной'

    form = ArtilesForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'news/create.html', data)