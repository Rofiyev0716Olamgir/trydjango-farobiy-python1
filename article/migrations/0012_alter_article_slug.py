# Generated by Django 5.0 on 2023-12-12 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0011_alter_article_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
    ]
