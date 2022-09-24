# Generated by Django 4.1.1 on 2022-09-23 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscribers', '0003_alter_subscriber_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=128)),
                ('url', models.CharField(max_length=128)),
                ('start_time', models.CharField(max_length=128)),
                ('end_time', models.CharField(max_length=128)),
                ('duration', models.CharField(max_length=128)),
                ('description', models.CharField(max_length=128)),
                ('in_24_hours', models.CharField(max_length=128)),
            ],
            options={
                'verbose_name_plural': 'Contests',
            },
        ),
        migrations.AlterModelOptions(
            name='subscriber',
            options={'verbose_name': 'Subscriber', 'verbose_name_plural': 'Subscribers'},
        ),
    ]