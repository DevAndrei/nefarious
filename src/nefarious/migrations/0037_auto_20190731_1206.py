# Generated by Django 2.1.5 on 2019-07-31 12:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nefarious', '0036_auto_20190731_1205'),
    ]

    operations = [
        migrations.RenameField(
            model_name='nefarioussettings',
            old_name='keyword_filters',
            new_name='keyword_search_filters',
        ),
    ]
