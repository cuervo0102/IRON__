# Generated by Django 4.2.5 on 2023-09-15 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sellerprofile',
            name='phone_number',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='sellerprofile',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]