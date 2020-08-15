from django.db import models
from django.utils.text import slugify


class GeeksModel(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    slug = models.SlugField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.title and not self.slug:
            self.slug = slugify(self.title)
        super(GeeksModel, self).save(*args, *kwargs)

    def __str__(self):
        return self.title
