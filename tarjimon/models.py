from django.db import models
class Lugat(models.Model):
    inglizcha = models.CharField('Inglizcha', max_length=130)
    uzbekcha = models.CharField('Uzbekcha', max_length=130)
    
    class Meta:
        verbose_name = "Lugat"
        verbose_name_plural = "Lugatlar"