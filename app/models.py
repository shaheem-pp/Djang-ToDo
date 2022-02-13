from django.db import models


# Create your models here.
class tbl_new_task(models.Model):
    title = models.CharField(max_length=500)
    status = models.CharField(max_length=10, default="current")
