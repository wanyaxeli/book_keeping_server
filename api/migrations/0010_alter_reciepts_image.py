# Generated by Django 4.2.1 on 2023-05-25 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_reciepts_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reciepts',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]