# Generated by Django 3.1.7 on 2021-05-31 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0002_customer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_no', models.IntegerField(max_length=10)),
                ('rent', models.IntegerField(max_length=10)),
            ],
        ),
    ]
