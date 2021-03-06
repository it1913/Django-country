# Generated by Django 4.0.4 on 2022-05-24 06:25

import countries.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('countries', '0004_alter_country_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='country',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to=countries.models.attachment_path, verbose_name='Vlajka státu'),
        ),
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('file', models.FileField(null=True, upload_to=countries.models.attachment_path, verbose_name='File')),
                ('type', models.CharField(blank=True, choices=[('audio', 'Audio'), ('image', 'Image'), ('text', 'Text'), ('video', 'Video'), ('other', 'Other')], default='image', help_text='Select allowed attachment type', max_length=5, verbose_name='Attachment type')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='countries.country')),
            ],
            options={
                'ordering': ['-last_update', 'type'],
            },
        ),
    ]
