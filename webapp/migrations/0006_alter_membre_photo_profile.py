# Generated by Django 5.1.2 on 2024-10-29 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0005_alter_membre_photo_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membre',
            name='photo_profile',
            field=models.ImageField(null=True, upload_to='media/photos/'),
        ),
    ]
