# Generated by Django 4.2.7 on 2023-11-03 22:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_address_zip'),
    ]

    operations = [
        migrations.RunSQL("""
            INSERT INTO store_collection(title)
            VALUE('collection1')                  
        """, """
            DELETE FROM store_collection
            WHERE title='collection1'
        """)
    ]