# Generated by Django 4.1.1 on 2023-05-01 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='emailverification',
            name='email_verification_code',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
