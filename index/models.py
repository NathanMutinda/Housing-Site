from django.db import models

# Create your models here.


class House(models.Model):
    h_name = models.CharField(max_length=100, blank=True)
    picture = models.ImageField(blank=True, null=True, default='cart.png')
    rent = models.IntegerField(default=0, null=True, blank=True)
    location = models.CharField(max_length=100, blank=True)
    Landlord_no = models.IntegerField(default=0, blank=True, null=True)
    caretaker_no = models.IntegerField(default=0, blank=True, null=True)
    favorite = models.BooleanField(default=False, blank=True, null=True)
    status = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.h_name

    @property
    def imageURL(self):
        try:
            url = self.picture.url
        except:
            url = ''
            return url


class Details(models.Model):
    user_name = models.CharField(max_length=100, blank=True)
    thumbnail = models.ImageField(null=True, blank=True)
    comment = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.user_name







