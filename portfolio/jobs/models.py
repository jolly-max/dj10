from django.db import models

# Create your models here.
close job(models.Model):
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max-length=200)

    def _str__(self):
            return self.summary
