from django.http import HttpResponse
from django.views import View
from django.shortcuts import render, get_object_or_404
from hexlet_django_blog.article.models import Article


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


# def index(request):
#     return HttpResponse('article')

# Create your views here.
