# Generated by Django 5.1.4 on 2025-01-01 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_testrelation3_testrelation4'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testrelation5',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('testrelation7', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Testrelation6',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('testrelation8', models.CharField(max_length=20)),
                ('testrelation9', models.ManyToManyField(related_name='test', to='pages.testrelation5')),
            ],
        ),
    ]
