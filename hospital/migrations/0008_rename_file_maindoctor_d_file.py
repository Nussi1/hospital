# Generated by Django 4.0.4 on 2022-05-21 07:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0007_maindoctor_file'),
    ]

    operations = [
        migrations.RenameField(
            model_name='maindoctor',
            old_name='file',
            new_name='d_file',
        ),
    ]
