# Generated by Django 2.1.5 on 2020-09-29 01:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0015_auto_20200929_0921'),
    ]

    operations = [
        migrations.RenameField(
            model_name='status_detail',
            old_name='name',
            new_name='detail',
        ),
    ]
