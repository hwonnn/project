# Generated by Django 4.2.3 on 2023-07-11 19:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Comment', '0002_alter_comment_table'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feed_post',
            name='already_like',
        ),
    ]
