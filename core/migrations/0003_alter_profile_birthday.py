# Generated by Django 4.0.3 on 2022-03-15 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='birthday',
            field=models.DateTimeField(null=True, verbose_name='Aniversário'),
        ),
    ]