from django.shortcuts import render, redirect
from .models import Artiles
from .forms import ArtilesForm

def news_home(request):
    news = Artiles.objects.order_by('-date') #Сортируем по дате публикации
    return render(request, 'news/news_home.html', {'news': news})

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