# Generated by Django 4.0.1 on 2022-01-18 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_alter_contact_phone_alter_order_phone_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(default='', max_length=70),
        ),
        migrations.AlterField(
            model_name='order',
            name='phone',
            field=models.CharField(default='', max_length=70),
        ),
        migrations.AlterField(
            model_name='order',
            name='zip',
            field=models.CharField(default='', max_length=70),
        ),
    ]
