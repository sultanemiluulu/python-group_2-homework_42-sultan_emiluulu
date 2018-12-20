from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name='Client name')
    email = models.EmailField(max_length=100, null=True, blank=True, verbose_name='Email')
    password = models.CharField(max_length=16, null=False, blank=False, verbose_name='Password')

    def __str__(self):
        return self.name


class Article(models.Model):
    headline = models.CharField(max_length=100, null=False, blank=False, verbose_name='Headline')
    text = models.TextField(max_length=2000, null=False, blank=False, verbose_name='Text')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created time')

    def __str__(self):
        return "%s. %s" % (self.pk, self.headline)