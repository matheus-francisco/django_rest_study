# Generated by Django 2.2.5 on 2019-09-06 01:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles_api', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='StatusUpdate',
            new_name='ProfileFeedItem',
        ),
        migrations.DeleteModel(
            name='Message',
        ),
    ]
