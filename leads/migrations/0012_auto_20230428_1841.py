# Generated by Django 3.1.4 on 2023-04-28 18:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0011_auto_20210218_1128'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Lead',
            new_name='Prospect',
        ),
    ]
