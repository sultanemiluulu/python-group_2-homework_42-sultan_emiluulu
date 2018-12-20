from django.contrib import admin
from webapp.models import Client, Article, Comment, Rating

admin.site.register(Client)
admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(Rating)
