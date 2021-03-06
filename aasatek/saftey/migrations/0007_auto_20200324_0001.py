# Generated by Django 2.2.11 on 2020-03-24 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saftey', '0006_auto_20200323_2340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='saftey',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='saftey',
            name='division',
            field=models.CharField(choices=[('Latemodel', 'Latemodel'), ('Jr latemodel', 'Jr latemodel'), ('Limited modifieds', 'Limited modifieds'), ('Super Stock', 'Super Stock'), ('F4', 'F4'), ('Mini Cup / Bandoleros', 'Mini Cup / Bandoleros'), ('Trailer', 'Trailer'), ('UTV', 'UTV'), ('Enduro', 'Enduro')], max_length=20),
        ),
        migrations.AlterField(
            model_name='saftey',
            name='helmetDate',
            field=models.CharField(choices=[('SA2012', 'SA2020'), ('SA2015', 'SA2015'), ('SA2010', 'SA2010'), ('Out Datad', 'Out Dated')], max_length=20),
        ),
        migrations.AlterField(
            model_name='saftey',
            name='recheck',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=20),
        ),
    ]
