from datetime import datetime, timedelta
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToCover
from django.db import models


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Picture(models.Model):

    class NonTrashManager(models.Manager):
        """ Query only objects which have not been trashed. """
        def get_queryset(self):
            query_set = super(Picture.NonTrashManager, self).get_queryset()
            return query_set.filter(trashed_time__isnull=True)

    class TrashManager(models.Manager):
        """ Query only objects which have been trashed. """
        def get_queryset(self):
            query_set = super(Picture.TrashManager, self).get_queryset()
            return query_set.filter(trashed_time__isnull=False)

    id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to='uploads/')
    image_small = ImageSpecField(
        source='image',
        processors=[ResizeToCover(300, 300)],
        format='JPEG',
        options={'quality': 80}
    )
    category = models.ForeignKey(
        'Category',
        on_delete=models.PROTECT
    )
    title = models.CharField(max_length=128)
    description = models.TextField(max_length=5120, blank=True)

    upload_time = models.DateField(auto_now_add=True)
    trashed_time = models.DateTimeField(blank=True, null=True)

    objects = NonTrashManager()
    trash = TrashManager()

    @property
    def is_trashed(self):
        return self.trashed_time is not None

    def delete(self, trash=True, **kwargs):
        if self.is_trashed or not trash:
            super(Picture, self).delete()
            return

        self.trashed_time = datetime.now()
        self.save()

    def restore(self, commit=True):
        self.trashed_time = None
        if commit:
            self.save()

    def __str__(self):
        if self.title:
            return f'An image #{self.id} with title \'{self.title}\''
        if self.description:
            description = (self.description[:128] + '...') if len(self.description) > 128 else self.description
            return f'An image #{self.id} with description \'{description}\''
        return f'An image #{self.id}'

    @staticmethod
    def clear_obsolete_trash():
        minute_ago = datetime.now() - timedelta(minutes=1)
        Picture.trash.filter(trashed_time__lt=minute_ago).delete()
