from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
# Category


# Category
class Category(models.Model):

    name = models.CharField(max_length=100)

    description = models.TextField()

    def __str__(self):
        return self.name


# Topic
class Topic(models.Model):

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )

    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


# Protocol
class Protocol(models.Model):

    topic = models.ForeignKey(
        Topic,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.topic.title


# Steps
class Step(models.Model):

    protocol = models.ForeignKey(
        Protocol,
        on_delete=models.CASCADE
    )

    step_number = models.IntegerField()

    description = RichTextUploadingField()

    image = models.ImageField(
        upload_to='steps/',
        null=True,
        blank=True
    )

    video_url = models.URLField(
        null=True,
        blank=True
    )

    def __str__(self):
        return f"Step {self.step_number}"