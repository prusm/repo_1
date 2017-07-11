from django.db import models
from django.utils import timezone


class Post(models.Model): #class = stworz obiet, post = nazwa modelu
#models.Model w ten spsosb django wie ze tworzymy obbiekt django i przechowuje go w bazie
    author = models.ForeignKey('auth.User')#odnosnik do innego modelu
    title = models.CharField(max_length=200) #tresc o ograniczonej ilosci znakow
    text = models.TextField()#nie ma ograniczonej ilosci znakow
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
