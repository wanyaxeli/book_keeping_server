# Generated by Django 4.2.1 on 2023-05-23 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_delete_sales'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('date', models.CharField(max_length=255)),
                ('items', models.JSONField(blank=True, max_length=1000, null=True)),
                ('total', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]