from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    group = models.ForeignKey('Group', on_delete=models.CASCADE, blank=True, null=True, related_name='posts')

    # ---------- ДОБАВЛЕНО ДЛЯ ТЕМЫ 2 (сериализатор) ----------
    def to_dict(self):
        return {
            'id': self.id,
            'text': self.text,
            'pub_date': self.pub_date.isoformat(),
            'author': self.author.username,
            'group': self.group.title if self.group else None,
        }

class Group(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()

    def __str__(self):
        return self.title