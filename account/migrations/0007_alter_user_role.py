# Generated by Django 3.2.16 on 2023-04-23 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_auto_20221106_2328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('employer', 'Shop Owner')], max_length=10),
        ),
    ]