from django.contrib.auth.models import User
from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True)
    updated_at = models.DateTimeField(
        auto_now=True)

    class Meta:
        abstract = True


class Post(BaseModel):
    user = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name='posts')
    title = models.CharField(
        max_length=255)
    image = models.ImageField(
        upload_to='posts/', blank=True, null=True)
    text = models.TextField()

    def __str__(self):
        return f'{self.id} - {self.user} - ({self.created_at})'
