# Generated by Django 3.0.5 on 2020-06-02 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ActivityPeriod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=9)),
                ('start_time', models.TextField()),
                ('end_time', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.CharField(max_length=9, primary_key=True, serialize=False)),
                ('real_name', models.CharField(max_length=25)),
                ('tz', models.CharField(max_length=25)),
            ],
        ),
    ]
