# Generated by Django 4.2.5 on 2023-10-13 09:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='password',
            new_name='number',
        ),
    ]
