# Generated by Django 4.0.4 on 2022-05-22 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0009_treatdoctor_bio_treatdoctor_d_file_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='subject',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='customer',
            name='text',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]
