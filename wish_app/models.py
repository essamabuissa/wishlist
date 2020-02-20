from django.db import models
from django.contrib.auth.models import User

class Item(models.Model):
    owner = models.ForeignKey(User, null = True, blank = True ,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    url = models.URLField(blank = True, null =True)
    timeadd = models.DateTimeField(auto_now_add=True, blank=True)
    image = models.ImageField(upload_to='Items_images', null=True, blank=True)
    is_purchased = models.BooleanField(default = False)
    purchased_by = models.CharField(max_length = 100)
    def __str__(self):
        return self.name
