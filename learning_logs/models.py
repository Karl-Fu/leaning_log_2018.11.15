from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Topic(models.Model):
    # '用户学习的主题'
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        # '返回模型的字符串表示'
        return self.text


class Entry(models.Model):
    # '为主题的具体条目定义模型'
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):

        if(len(self.text) > 50):
            return self.text[:50]+"..."
        else:
            return self.text

##---------------------------------以下为pizza店的练习----------------------------------##


class Pizza(models.Model):
    # '用户学习的主题'
    name = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # '返回模型的字符串表示'
        return self.name


class Topping(models.Model):
    # '为主题的具体条目定义模型'
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    name = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'toppings'

    def __str__(self):

        return self.name
