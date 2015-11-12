from django.db import models


# Create your models here.
class Shortcut(models.Model):
    shortcut_cmd = models.CharField(max_length=200)
    shortcut_desc = models.TextField()
    
    def __str__(self):
        return self.shortcut_cmd


class Choices(models.Model):
    FIRST_KEY = (
        ('Ctrl', 'Ctrl'),
        ('Shift', 'Shift'),
        ('Alt', 'Alt'),
    )
    SECOND_KEY = (
        ('C', 'C'),
        ('V', 'V'),
        ('S', 'S'),
        ('A', 'A'),
        ('Delete', 'Delete'),
        ('Enter', 'Enter'),
    )
    name = models.ForeignKey(Shortcut)
    first_key = models.CharField(max_length=10, choices=FIRST_KEY)
    second_key = models.CharField(max_length=10, choices=SECOND_KEY)