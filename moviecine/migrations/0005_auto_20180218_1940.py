# Generated by Django 2.0.2 on 2018-02-18 22:40

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('moviecine', '0004_auto_20180218_0019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='slug',
            field=models.SlugField(max_length=200),
        ),
    ]
