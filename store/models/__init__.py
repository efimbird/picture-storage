from django.db import models


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Picture(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to='uploads/')
    category = models.ForeignKey(
        'Category',
        on_delete=models.PROTECT
    )
    title = models.CharField(max_length=128)
    description = models.TextField(max_length=5120, blank=True)
    upload_time = models.DateField(auto_now_add=True)

    def __str__(self):
        if self.title:
            return f'An image #{self.id} with title \'{self.title}\''
        if self.description:
            description = (self.description[:128] + '...') if len(self.description) > 128 else self.description
            return f'An image #{self.id} with description \'{description}\''
        return f'An image #{self.id}'
