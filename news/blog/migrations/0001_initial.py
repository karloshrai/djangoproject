# Generated by Django 3.1.7 on 2021-04-10 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SettingModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=200)),
                ('company_email', models.CharField(max_length=200)),
                ('company_phone', models.CharField(max_length=100)),
                ('company_address', models.CharField(max_length=200)),
                ('company_logo', models.ImageField(null=True, upload_to='logo')),
                ('company_fax', models.IntegerField(null=True)),
            ],
        ),
    ]
