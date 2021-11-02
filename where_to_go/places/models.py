from django.db import models


class Place(models.Model):

    title = models.CharField(max_length=200)
    description_short = models.TextField()
    description_long = models.TextField()
    lng = models.FloatField()
    lat = models.FloatField()

    def __str__(self):
        return self.title

    class Meta(object):
        ordering = ['title']


class Image(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(verbose_name='Картинка')
    img_number = models.IntegerField()

    def __str__(self):
        return f'{self.img_number} {str(self.place)}'

    class Meta:
        ordering = ["img_number"]








