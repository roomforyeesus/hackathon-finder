# Generated by Django 4.1.1 on 2022-09-22 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscribers', '0002_alter_subscriber_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscriber',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
