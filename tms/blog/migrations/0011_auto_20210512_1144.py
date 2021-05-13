# Generated by Django 3.2 on 2021-05-12 05:59

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0010_auto_20210512_1126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blognews',
            name='created_at',
            field=models.DateTimeField(verbose_name=datetime.datetime(2021, 5, 12, 5, 59, 40, 998905, tzinfo=utc)),
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_date', models.DateField()),
                ('status', models.BooleanField(default=0)),
                ('package_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.package')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]