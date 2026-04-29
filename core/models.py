from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
# Category
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


# Topic
class Topic(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


# Protocol
class Protocol(models.Model):
    ROLE_CHOICES = (
        ('doctor', 'Doctor'),
        ('nurse', 'Nurse'),
    )

    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.topic} - {self.role}"

#steps
class Step(models.Model):
    protocol = models.ForeignKey('Protocol', on_delete=models.CASCADE)
    step_number = models.IntegerField()
    description = RichTextUploadingField()

    image = models.ImageField(upload_to='steps/', null=True, blank=True)
    video_url = models.URLField(null=True, blank=True)

    def __str__(self):
        return f"Step {self.step_number}"

# User Profile (Roles)
class Profile(models.Model):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('doctor', 'Doctor'),
        ('nurse', 'Nurse'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    def __str__(self):
        return self.user.username

from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=Topic)
def create_protocols(sender, instance, created, **kwargs):
    if created:
        Protocol.objects.create(topic=instance, role='doctor')
        Protocol.objects.create(topic=instance, role='nurse')