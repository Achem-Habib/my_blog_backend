
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
    summary = models.TextField()
    date = models.DateField()
    published = models.BooleanField(default=False)
    table_of_contents = models.TextField()
    body = models.TextField()


class Subscriber(models.Model):
    email = models.EmailField()
    date_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-date_time"]

    def __str__(self):
        return self.email
