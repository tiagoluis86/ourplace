# Generated by Django 4.0.3 on 2022-03-16 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_profile_birthday'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='id',
            field=models.BigIntegerField(primary_key=True, serialize=False),
        ),
    ]
