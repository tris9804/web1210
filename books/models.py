from django.db import models

class Book(models.Model):
    name = models.CharField(max_length=20)
    price = models.PositiveIntegerField()
    introduction = models.TextField()

    def __str__(self):
        return '{} ({})'.format(self.name, self.id)
        


