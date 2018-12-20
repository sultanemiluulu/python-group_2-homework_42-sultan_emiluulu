from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
from webapp.models import Client, Article, Comment, Rating
from webapp.forms import SearchArticleForm, ArticleCreateForm, ArticleUpdateForm, CommentCreateForm, CommentUpdateForm
from django.urls import reverse_lazy


class ArticleListView(ListView, FormView):
    model = Article
    template_name = 'article_list.html'
    form_class = SearchArticleForm

    def get_queryset(self):
        article_name = self.request.GET.get('article_name')
        if article_name:
            return Article.objects.filter(headline__icontains=article_name)
        else:
            return Article.objects.all()


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_detail.html'


class ArticleCreateView(CreateView):
    model = Article
    template_name = 'article_create.html'
    form_class = ArticleCreateForm
    success_url = reverse_lazy('article_list')


class ArticleUpdateView(UpdateView):
    model = Article
    template_name = 'article_update.html'
    form_class = ArticleUpdateForm
    success_url = reverse_lazy('article_list')


class CommentCreateView(CreateView):
    model = Comment
    template_name = 'comment_create.html'
    form_class = CommentCreateForm
    success_url = reverse_lazy('article_list')


class CommentUpdateView(UpdateView):
    model = Comment
    template_name = 'comment_update.html'
    form_class = CommentUpdateForm
    success_url = reverse_lazy('article_list')


class ClientListView(ListView):
    model = Client
    template_name = 'client_list.html'


class ClientDetailView(DetailView):
    model = Client
    template_name = 'client_detail.html'