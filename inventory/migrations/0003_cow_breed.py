# Generated by Django 3.1.7 on 2021-04-08 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_auto_20210402_1216'),
    ]

    operations = [
        migrations.AddField(
            model_name='cow',
            name='breed',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
