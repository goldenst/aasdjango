# Generated by Django 2.2.11 on 2020-03-24 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saftey', '0008_remove_saftey_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='saftey',
            name='seatbeltDate',
            field=models.CharField(max_length=20),
        ),
    ]
