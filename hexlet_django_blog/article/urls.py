from django.urls import path
# from hexlet_django_blog.article import views
from hexlet_django_blog.article.views import IndexView, ArticleByID, ArticleView, ArticleFormCreateView

urlpatterns = [
    path('', IndexView.as_view(), name='articles'),
    path('<int:id>/', ArticleView.as_view(), name='article_id'),
    path('<str:tags>/<int:article_id>/', ArticleByID.as_view()),
    path('create/', ArticleFormCreateView.as_view(), name='articles_create'),
]
