# Generated by Django 3.0.6 on 2020-05-29 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exampleapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='title')),
                ('teaser', models.TextField(verbose_name='teaser')),
                ('body', models.TextField(verbose_name='body')),
                ('views', models.IntegerField(default=0, verbose_name='views')),
                ('average_note', models.FloatField(default=0, verbose_name='average_note')),
                ('commentable', models.BooleanField(default=True, verbose_name='commentable')),
                ('published_at', models.DateField(auto_now_add=True, verbose_name='published_at')),
                ('category', models.CharField(blank=True, max_length=100, verbose_name='category')),
                ('subcategory', models.CharField(blank=True, max_length=100, verbose_name='subcategory')),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
            },
        ),
    ]
