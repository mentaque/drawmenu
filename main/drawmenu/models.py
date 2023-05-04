from django.db import models


class MenuItem(models.Model):
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=255, unique=True)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'

    def __str__(self):
        return self.name