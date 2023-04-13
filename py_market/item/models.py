from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta: 
        ordering=('name',)
        verbose_name_plural ="Categories"
    
    #this ensures the item names show up properly in the admin page
    def __str__(self):
        return self.name