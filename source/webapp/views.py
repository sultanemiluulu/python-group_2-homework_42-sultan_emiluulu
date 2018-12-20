from django.views.generic import ListView, DetailView
from webapp.models import Client, Article, Comment, Rating


class ArticleListView(ListView):
    model = Article
    template_name = 'article_list.html'


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_detail.html'


class ClientListView(ListView):
    model = Client
    template_name = 'client_list.html'


class ClientDetailView(DetailView):
    model = Client
    template_name = 'client_detail.html'