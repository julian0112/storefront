# Generated by Django 4.2.7 on 2023-11-03 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_add_slug_to_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='zip',
            field=models.CharField(default='-', max_length=255),
            preserve_default=False,
        ),
    ]
