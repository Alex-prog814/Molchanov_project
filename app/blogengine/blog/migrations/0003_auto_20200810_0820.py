# Generated by Django 2.0.7 on 2020-08-10 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200806_1629'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-date_pub']},
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={'ordering': ['title']},
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(blank=True, max_length=150, unique=True),
        ),
    ]
