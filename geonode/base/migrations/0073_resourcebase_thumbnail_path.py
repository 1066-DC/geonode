# Generated by Django 3.2.4 on 2021-11-12 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0072_remove_resourcebase_detail_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='resourcebase',
            name='thumbnail_path',
            field=models.TextField(blank=True, null=True, verbose_name='Thumbnail path'),
        ),
    ]
