# Generated by Django 2.1.2 on 2018-11-08 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='bag',
            field=models.CharField(default='SOME STRING', max_length=200),
        ),
        migrations.AddField(
            model_name='note',
            name='down',
            field=models.TextField(default='SOME STRING'),
        ),
        migrations.AddField(
            model_name='note',
            name='elb',
            field=models.CharField(default='SOME STRING', max_length=200),
        ),
        migrations.AddField(
            model_name='note',
            name='fox',
            field=models.TextField(default='SOME STRING'),
        ),
        migrations.AddField(
            model_name='note',
            name='gaot',
            field=models.CharField(default='SOME STRING', max_length=200),
        ),
        migrations.AddField(
            model_name='note',
            name='horse',
            field=models.TextField(default='SOME STRING'),
        ),
        migrations.AlterField(
            model_name='note',
            name='body',
            field=models.TextField(default='SOME STRING'),
        ),
    ]
