from django.db import models
from django.contrib.auth.models import User
from cloudinary_storage.storage import RawMediaCloudinaryStorage
# Create your models here.

class Feed(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    caption = models.TextField()
    image = models.ImageField(upload_to='uploads/', storage=RawMediaCloudinaryStorage(),null=True,blank=True)
    created_on = models.DateTimeField(auto_now_add=True,null=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user)


class Comments(models.Model):
    feed = models.ForeignKey(Feed,on_delete=models.CASCADE)
    thought = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True,null=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.created_on)
    


class Like(models.Model):
    feed = models.ForeignKey(Feed, on_delete=models.CASCADE)
    liked_by = models.CharField(max_length=200)
    liked_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Like by {self.liked_by} on {self.liked_at}"

