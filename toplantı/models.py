from django.db import models

# Create your models here.
class Toplantı(models.Model):
    name =models.CharField(max_length=100, verbose_name='Toplantı Konu')
    tarih = models.DateTimeField(auto_now=True, verbose_name='Tarih')
    description=models.TextField(verbose_name='Katılımcılar')
    isPublished=models.BooleanField(default=True)
    bsal = models.CharField(max_length=100,default='SOME STRING', verbose_name='Bsal')
    ssal = models.CharField(max_length=100,default='SOME STRING', verbose_name='Ssal')

    def __str__(self):
        return self.name