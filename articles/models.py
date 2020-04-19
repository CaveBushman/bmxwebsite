from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    #author = models.CharField()

    on_headline = models.BooleanField(default=False)
    headline_positions = models.IntegerField()

    path_to_image = models.CharField(max_length=255, null = True, blank = True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title