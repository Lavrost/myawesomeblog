# Generated by Django 3.1.2 on 2020-10-29 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20201028_0640'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to='posts_images/'),
        ),
    ]
