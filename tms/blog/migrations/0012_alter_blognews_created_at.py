# Generated by Django 3.2 on 2021-05-12 16:42

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20210512_1144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blognews',
            name='created_at',
            field=models.DateTimeField(verbose_name=datetime.datetime(2021, 5, 12, 16, 42, 26, 819593, tzinfo=utc)),
        ),
    ]