from django.contrib import admin
from webapp.models import Client, Article, Comment, Rating

class UserAdmin(admin.ModelAdmin):
    filter_horizontal = ('favorites',)

admin.site.register(Client, UserAdmin)
admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(Rating)
