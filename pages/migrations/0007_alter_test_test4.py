# Generated by Django 5.1.4 on 2025-01-01 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_testrelation5_testrelation6'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='test4',
            field=models.CharField(max_length=20),
        ),
    ]