from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Product(models.Model):
    ranking = models.CharField('RANK', max_length=10, blank=True, null=True)
    title = models.CharField(verbose_name='TITLE', max_length=100)
    price = models.CharField('PRICE', max_length=20, null=True)
    sat_count = models.CharField('NUMBER_OF_REVIEWS', max_length=20, null=True)
    score = models.CharField('SCORE', max_length=20, null=True)
    image = models.ImageField('IMAGE', upload_to='ProductImages', blank=True, null=True)

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'
        db_table = 'crawl_products'
        ordering = ('-ranking',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('crawl:product_detail', args=(self.pk,))

    def get_previous(self):
        return self.get_previous_by_modify_dt()

    def get_next(self):
        return self.get_next_by_modify_dt()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
