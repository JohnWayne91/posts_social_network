from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.pk)


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    body = models.CharField(max_length=500)

    def __str__(self):
        return str(self.title)
