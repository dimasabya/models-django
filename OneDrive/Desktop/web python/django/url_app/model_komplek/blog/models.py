from django.db import models

# Create your models here.
class Data(models.Model):
    judul = models.CharField(max_length=20, blank=True);
    body = models.TextField();
    email = models.EmailField(default='nama@gmail.com');
    alamat = models.CharField(max_length=200, blank=True);
    waktu = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}'.format(self.judul)