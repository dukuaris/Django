# Generated by Django 2.2.6 on 2020-03-19 15:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crawl', '0006_auto_20200319_1525'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('-ranking',), 'verbose_name': 'product', 'verbose_name_plural': 'products'},
        ),
        migrations.RenameField(
            model_name='product',
            old_name='rank',
            new_name='ranking',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='review',
            new_name='sat_count',
        ),
        migrations.RemoveField(
            model_name='product',
            name='create_dt',
        ),
        migrations.RemoveField(
            model_name='product',
            name='owner',
        ),
    ]
