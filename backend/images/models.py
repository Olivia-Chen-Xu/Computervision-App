from django.db import models

# Create your models here.

class Image(models.Model):
    picture = models.ImageField()
    classified = models.CharField(max_length=200, blank=True)
    upload = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return "Image classified at {}".format(self.upload.strftime('%Y-%m-%d %H:%M'))

    def save(self, *args, **kwargs):
        try:
            img = load_img(self.picture, target_size=(299,299))
            print(img)
        except:
            print('classification failed')
        super().save(*args, **kwargs)
