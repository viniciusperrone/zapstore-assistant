# Generated by Django 5.2.1 on 2025-05-18 23:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='inflows',
            options={'ordering': ['-created_at']},
        ),
    ]
