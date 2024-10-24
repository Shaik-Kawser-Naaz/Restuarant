from django.db import models

# Create your models here.
class Food(models.Model):
    name=models.CharField(max_length=50)
    variety=models.CharField(max_length=50)
    price=models.IntegerField()

    def _str_(self):
        return self.item