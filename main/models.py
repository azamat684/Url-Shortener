from django.db import models

class ShortenedURL(models.Model):
    long_url = models.URLField(unique=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.slug
    
    
class ShortURLList(models.Model):
    shortened_url = models.ForeignKey(ShortenedURL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']