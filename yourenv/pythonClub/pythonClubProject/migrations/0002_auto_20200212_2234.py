# Generated by Django 3.0.1 on 2020-02-12 22:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pythonClubProject', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='meeting_minutes',
            options={'verbose_name_plural': 'Meeting_Minutes'},
        ),
        migrations.AlterModelTable(
            name='meeting_minutes',
            table='Meeting_Minutes',
        ),
    ]
