# Generated by Django 2.0.2 on 2018-02-17 17:05

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('image', models.FileField(upload_to='actors')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('original_title', models.CharField(max_length=255)),
                ('duration', models.BigIntegerField(default=0)),
                ('slug', models.CharField(max_length=200)),
                ('synopsis', models.TextField()),
                ('image', models.FileField(upload_to='movies/%Y/%m/%d')),
                ('likes', models.BigIntegerField(default=0)),
                ('published', models.BooleanField(default=False)),
                ('actors', models.ManyToManyField(related_name='actors', to='moviecine.Actor')),
            ],
        ),
    ]
