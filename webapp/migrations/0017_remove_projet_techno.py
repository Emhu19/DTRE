# Generated by Django 5.1.2 on 2024-11-02 18:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0016_techno_remove_event_date_event_date_debut_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projet',
            name='techno',
        ),
    ]
