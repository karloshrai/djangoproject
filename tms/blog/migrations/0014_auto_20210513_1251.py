# Generated by Django 3.2 on 2021-05-13 07:06

import ckeditor.fields
import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20210513_0017'),
    ]

    operations = [
        migrations.CreateModel(
            name='Terms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', ckeditor.fields.RichTextField()),
            ],
        ),
        migrations.AlterField(
            model_name='blognews',
            name='created_at',
            field=models.DateTimeField(verbose_name=datetime.datetime(2021, 5, 13, 7, 6, 32, 879075, tzinfo=utc)),
        ),
    ]
