# Generated by Django 2.2.6 on 2020-03-19 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crawl', '0003_auto_20200319_1432'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='description',
        ),
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(max_length=100, verbose_name='TITLE'),
        ),
    ]
