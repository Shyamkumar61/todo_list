from django.db import models
from django_extensions.db.models import CreationDateTimeField, ModificationDateTimeField


# Create your models here.
class BaseModel(models.Model):
    created = CreationDateTimeField(('created'))
    last_modified = ModificationDateTimeField('modified')

    class Meta:
        abstract = True

class newstats(models.Model):
    win = models.IntegerField(default=0)
    mac = models.IntegerField(default=0)
    iph = models.IntegerField(default=0)
    android = models.IntegerField(default=0)
    oth = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'New Stats'
        verbose_name_plural = 'New Stats'
class Todo_list(BaseModel):

    STATUS = (
        ('Completed', 'Completed'),
        ('Ongoing', 'Ongoing'),
        ('Pending', 'Pending')
    )

    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=100, choices=STATUS, default=None, null=True)

    class Meta:
        verbose_name = "Todo_list"
        verbose_name_plural = "Todo_lists"

    def __str__(self):
        return self.title


