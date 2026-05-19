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
    topic = models.OneToOneField(Topic, on_delete=models.CASCADE)

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
    

        # models.py
class About(models.Model):
    university_logo = models.ImageField(upload_to='about/logos/')
    project_name = models.CharField(max_length=200)
    description = models.TextField() # استخدم CKEditor هنا إذا أردت
    group_name = models.CharField(max_length=100)
    group_image = models.ImageField(upload_to='about_images/')
    
    def __str__(self):
        return self.project_name

class ProjectGoal(models.Model):
    about = models.ForeignKey(About, related_name='goals', on_delete=models.CASCADE)
    title = models.CharField(max_length=100) # مثال: "تحسين الكفاءة"
    description = models.TextField() # مثال: "رفع مستوى الأداء وتقليل الوقت"
    icon = models.ImageField(upload_to='goal_icons/') # أيقونة لكل هدف