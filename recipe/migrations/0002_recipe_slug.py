# Generated by Django 5.0 on 2023-12-16 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='slug',
            field=models.SlugField(editable=False, null=True, unique=True),
        ),
    ]
