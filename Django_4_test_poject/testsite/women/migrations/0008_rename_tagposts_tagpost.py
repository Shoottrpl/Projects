# Generated by Django 4.2.1 on 2024-03-13 19:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0007_tagposts_alter_women_cat_women_tags'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TagPosts',
            new_name='TagPost',
        ),
    ]