from django.db import models


class Note(models.Model):
    Length = models.CharField(max_length=200, default=0)
    AbsoluteLength = models.CharField(max_length=200,default=0)
    Duration = models.CharField(max_length=200, default=0)
    AvgSpeed = models.CharField(max_length=200,default=0)
    AvgPressure = models.CharField(max_length=200, default=0)
    StartX = models.CharField(max_length=200,default=0)
    StartY = models.CharField(max_length=200, default=0)
    EndX = models.CharField(max_length=200,default=0)
    EndY = models.CharField(max_length=200, default=0)
    MoveType = models.TextField(max_length=200, default='null')
    UserID = models.TextField(max_length=200, default='null')
    created_at = models.DateTimeField(auto_now_add=True)


def __str__(self):
    # return self.title
    return '%s %s' % (self.title, self.body)
# Create your models here.
