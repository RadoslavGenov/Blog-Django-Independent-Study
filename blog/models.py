from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify
from taggit.managers import TaggableManager
import itertools


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset()


class Post(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(unique=True)
    author = models.CharField(max_length=100)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    objects = models.Manager()    #default manager
    published = PublishedManager()#custom manager
    
    class Meta:
        ordering = ('-publish',)
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail',
                       args=[self.publish.year,
                             self.publish.strftime('%m'),
                             self.publish.strftime('%d'),
                             self.slug]
                       )

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
            for x in itertools.count(1):
                if not Post.objects.filter(slug=self.slug).exists():
                    break
                self.slug = '%s-%d' % (self.slug, x)
            super(Post, self).save(*args, **kwargs)

    tags = TaggableManager()


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ('created',)
        
    def __str__(self):
        return "Comment by {} on {} created on {}".format(self.name, self.post, self.created)



