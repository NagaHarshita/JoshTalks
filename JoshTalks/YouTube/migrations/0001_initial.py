# Generated by Django 3.2.9 on 2021-11-18 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_id', models.CharField(max_length=30)),
                ('title', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=250)),
                ('channel_id', models.CharField(max_length=30)),
                ('channel_title', models.CharField(max_length=30)),
                ('published_time', models.DateTimeField()),
            ],
        ),
    ]
