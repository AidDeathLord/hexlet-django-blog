from django.http import HttpResponse
from django.views import View
from django.shortcuts import render
from hexlet_django_blog.article.models import Article


class IndexView(View):
    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()[:15]
        return render(request, 'articles/index.html', context={'articles': articles})


class ArticleByID(View):
    def get(self, request, tags, article_id):
        return HttpResponse(f'Статья номер {article_id}. Тег {tags}')


# def index(request):
#     return HttpResponse('article')

# Create your views here.
