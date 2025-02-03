from django.db import models

# Create your models here.
class Comment(models.Model):
    name = models.CharField(
        max_length=155
    )
    comment = models.TextField()
    email = models.CharField(
        max_length=155
    )

    def __str__(self):
        return self.name

    class MEta:
        verbose_name_plural = 'Комментарий'