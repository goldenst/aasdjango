# Generated by Django 2.2 on 2020-03-25 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scales', '0002_auto_20200324_2004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scales',
            name='midRaceLeft',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True),
        ),
        migrations.AlterField(
            model_name='scales',
            name='midRaceStart',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='scales',
            name='preQualifingLeft',
            field=models.DecimalField(decimal_places=1, max_digits=3),
        ),
        migrations.AlterField(
            model_name='scales',
            name='raceStartLeft',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True),
        ),
        migrations.AlterField(
            model_name='scales',
            name='raceStartWeight',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
