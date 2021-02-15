# Generated by Django 3.1.4 on 2021-02-07 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0003_application'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='company_address',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='company_country',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='company_name',
            field=models.CharField(default='Default Name', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='job',
            name='company_place',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='company_size',
            field=models.CharField(choices=[('size_1-9', '1-9'), ('size_10-49', '10-49'), ('size_50-99', '50-99'), ('size_100', '100+')], default='size_1-9', max_length=20),
        ),
        migrations.AddField(
            model_name='job',
            name='company_zipcode',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
