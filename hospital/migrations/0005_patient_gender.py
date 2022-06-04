# Generated by Django 4.0.4 on 2022-05-20 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0004_rename_text_appointment_text_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='gender',
            field=models.CharField(choices=[('m', 'male'), ('f', 'female')], default=1, max_length=2),
            preserve_default=False,
        ),
    ]
