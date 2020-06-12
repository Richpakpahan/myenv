from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from django.urls import reverse_lazy

class Reference(models.Model):

    title = models.CharField(max_length=250)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reference_posts')
    description = models.TextField()
    slug = models.SlugField(max_length=250, blank=True)
    link = models.URLField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = models.Manager()

    class meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy('reference:reference_list')
    
    # def get_absolute_url(self):
    #     return reverse_lazy('reference:reference_detail', kwargs={'pk':self.id})
# Create your models here.
