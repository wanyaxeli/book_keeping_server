# Generated by Django 4.2.1 on 2023-05-24 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_sales'),
    ]

    operations = [
        migrations.AddField(
            model_name='reciepts',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]
