from django.db import models

# Create your models here.
class Job(models.Model):
    position = models.CharField(max_length=100)
    description = models.TextField()
    isactive = models.BooleanField(default=True)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.position

