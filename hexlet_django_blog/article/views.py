from django.http import HttpResponse
from django.views import View
from django.shortcuts import render, get_object_or_404, redirect
from hexlet_django_blog.article.models import Article
from .forms import ArticleForm


class IndexView(View):
    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()[:15]
        return render(request, 'articles/index.html', context={'articles': articles})


class ArticleView(View):
    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=kwargs['id'])
        return render(request, 'articles/show.html', context={'article': article})


class ArticleByID(View):
    def get(self, request, tags, article_id):
        return HttpResponse(f'Статья номер {article_id}. Тег {tags}')


class ArticleFormCreateView(View):
    def get(self, request, *args, **kwargs):
        form = ArticleForm()
        return render(request, 'articles/create.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = ArticleForm(request.POST)
        if form.is_valid():  # Если данные корректные, то сохраняем данные формы
            form.save()
            return redirect('articles')  # Редирект на указанный маршрут
        # Если данные некорректные, то возвращаем человека обратно на страницу с заполненной формой
        return render(request, 'articles/create.html', {'form': form})
# def index(request):
#     return HttpResponse('article')

# Create your views here.
