# Generated by Django 4.1.1 on 2022-09-23 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscribers', '0006_contests_delete_contest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscriber',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]