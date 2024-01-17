# Generated by Django 4.2.7 on 2023-11-23 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('ids', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('roll_number', models.IntegerField(default=100)),
                ('mobile_number', models.IntegerField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='img/')),
            ],
        ),
    ]
