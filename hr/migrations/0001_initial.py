# Generated by Django 3.1.7 on 2021-03-30 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=255, null=True)),
                ('second_name', models.CharField(blank=True, max_length=255, null=True)),
                ('fathers_name', models.CharField(blank=True, max_length=255, null=True)),
                ('mothers_name', models.CharField(blank=True, max_length=255, null=True)),
                ('home_district', models.CharField(blank=True, max_length=255, null=True)),
                ('spouse_occupation', models.CharField(blank=True, max_length=255, null=True)),
                ('religion', models.CharField(blank=True, max_length=255, null=True)),
                ('date_joined', models.DateField(blank=True, null=True)),
                ('entry_designation', models.CharField(blank=True, max_length=255, null=True)),
                ('entry_scale', models.CharField(blank=True, max_length=255, null=True)),
                ('picture', models.FileField(blank=True, null=True, upload_to='documents/%Y/%m/%d')),
                ('archive_status', models.CharField(blank=True, choices=[('yes', 'yes'), ('no', 'no')], max_length=32)),
                ('status', models.CharField(blank=True, choices=[('active', 'active'), ('inactive', 'inactive')], max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
    ]
