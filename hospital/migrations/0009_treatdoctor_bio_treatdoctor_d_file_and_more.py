# Generated by Django 4.0.4 on 2022-05-21 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0008_rename_file_maindoctor_d_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='treatdoctor',
            name='bio',
            field=models.CharField(default=1, max_length=2000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='treatdoctor',
            name='d_file',
            field=models.FileField(blank=True, upload_to='files/%Y/%m/%d'),
        ),
        migrations.AddField(
            model_name='treatdoctor',
            name='position',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
