# Generated by Django 2.1.5 on 2020-09-29 01:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0011_auto_20200929_0913'),
    ]

    operations = [
        migrations.RenameField(
            model_name='player',
            old_name='position',
            new_name='activity',
        ),
    ]
