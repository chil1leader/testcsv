from django.db import models
from django.contrib.postgres.fields import ArrayField


class Member(models.Model):
    customer = models.CharField(max_length=50)
    item = ArrayField(models.CharField(max_length=50))
    item_top_five = ArrayField(models.CharField(max_length=50), blank=True, null=True)
    total = models.IntegerField()

    def __str__(self):
        return self.customer