# Generated by Django 5.0.7 on 2024-10-16 08:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('texnomart_uz', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='authentication',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='authentication',
            new_name='user',
        ),
    ]
