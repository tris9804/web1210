# Generated by Django 2.1.4 on 2018-12-12 11:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_book_introdution'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='introdution',
            new_name='introduction',
        ),
    ]
