# Generated by Django 2.2.4 on 2022-01-10 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_page', '0008_auto_20220109_1753'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='confirmation',
            field=models.CharField(default='CONFIR', max_length=6),
        ),
    ]
