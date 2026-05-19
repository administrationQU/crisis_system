from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from cloudinary.models import CloudinaryField  
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

    image = CloudinaryField(
        'image',
        null=True,
        blank=True
    )

    video_url = models.URLField(
        null=True,
        blank=True
    )

    def __str__(self):
        return f"Step {self.step_number}"
    

from django.db import models
from cloudinary.models import CloudinaryField

# about
class About(models.Model):
    project_name = models.CharField(max_length=200)
    university_logo = CloudinaryField('image')
    college_logo = CloudinaryField('image') # تم تصحيح الاسم
    description = RichTextUploadingField() 
    group_name = models.CharField(max_length=100)
    group_image = CloudinaryField('image', blank=True, null=True) # أضفتها لتكتمل الصورة
    
    def __str__(self):
        return self.project_name

# نموذج الأهداف المرتبط بالمشروع
class ProjectGoal(models.Model):
    about = models.ForeignKey(About, related_name='goals', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = RichTextUploadingField()
    icon = CloudinaryField('image')

    def __str__(self):
        return f"{self.about.project_name} - {self.title}"