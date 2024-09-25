from django.urls import path
# from hexlet_django_blog.article import views
from hexlet_django_blog.article.views import IndexView, ArticleByID

urlpatterns = [
    path('', IndexView.as_view(), name='article'),
    path('<str:tags>/<int:article_id>/', ArticleByID.as_view(), name='article_id'),
]
