# Generated by Django 4.0.4 on 2022-05-24 06:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('countries', '0005_country_img_attachment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='attachment',
            old_name='country',
            new_name='img',
        ),
    ]