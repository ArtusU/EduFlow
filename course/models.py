from django.conf import settings
from django.contrib.auth.models import User
from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    short_description = models.TextField(blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title

class Course(models.Model):
    DRAFT = 'draft'
    IN_REVIEW = 'in_review'
    PUBLISHED = 'published'

    STATUS_CHOICES = (
        (DRAFT, 'Draft'),
        (IN_REVIEW, 'In review'),
        (PUBLISHED, 'Published')
    )

    categories = models.ManyToManyField(Category)
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    short_description = models.TextField(blank=True, null=True)
    long_description = models.TextField(blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='courses', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='uploads', blank=True, null=True)
    status = models.CharField(max_length=25, choices=STATUS_CHOICES, default=DRAFT)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.title

    def get_image(self):
        if self.image:
            return settings.WEBSITE_URL + self.image.url
        else:
            return 'http://bulma.io/images/placeholders/1280x960.png'
