from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField('タイトル', max_length=30)
    description = models.TextField('やること', blank=True)
    deadline = models.DateField('期限')

    def __str__(self):
        return self.title
        
