# Generated by Django 2.1.2 on 2018-11-08 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20181108_1557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='AvgPressure',
            field=models.CharField(default=100, max_length=200),
        ),
        migrations.AlterField(
            model_name='note',
            name='Duration',
            field=models.CharField(default=100, max_length=200),
        ),
        migrations.AlterField(
            model_name='note',
            name='EndY',
            field=models.CharField(default=100, max_length=200),
        ),
        migrations.AlterField(
            model_name='note',
            name='Length',
            field=models.CharField(default=100, max_length=200),
        ),
        migrations.AlterField(
            model_name='note',
            name='MoveType',
            field=models.CharField(default=100, max_length=200),
        ),
        migrations.AlterField(
            model_name='note',
            name='StartY',
            field=models.CharField(default=100, max_length=200),
        ),
        migrations.AlterField(
            model_name='note',
            name='UserID',
            field=models.CharField(default=100, max_length=200),
        ),
    ]
