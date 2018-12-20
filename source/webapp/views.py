from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
from webapp.models import Client, Article, Comment, Rating
from webapp.forms import SearchArticleForm
from django.urls import reverse_lazy


class ArticleListView(ListView, FormView):
    model = Article
    template_name = 'article_list.html'
    form_class = SearchArticleForm

    def get_queryset(self):
        article_name = self.request.GET.get('article_name')
        if not article_name:
            return Article.objects.all()
        else:
            return Article.objects.filter(headline__icontains=article_name)


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_detail.html'


class ClientListView(ListView):
    model = Client
    template_name = 'client_list.html'


class ClientDetailView(DetailView):
    model = Client
    template_name = 'client_detail.html'