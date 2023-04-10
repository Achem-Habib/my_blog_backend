from django.db import models
from django.utils.text import slugify


class Tag(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Tag, self).save(*args, **kwargs)


class Post(models.Model):
    tags = models.ManyToManyField(Tag)
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    image = models.ImageField(upload_to="images/")
    table_of_contents = models.TextField()
    summary = models.TextField()
    date = models.DateField()
    body = models.TextField()
    published = models.BooleanField(default=False)
    most_popular = models.BooleanField(default=False)

    class Meta:
        ordering = ["-date"]

    def __str__(self):
        return self.title