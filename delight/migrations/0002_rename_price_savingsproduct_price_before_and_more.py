# Generated by Django 4.1.3 on 2022-11-15 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delight', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='savingsproduct',
            old_name='price',
            new_name='price_before',
        ),
        migrations.AddField(
            model_name='savingsproduct',
            name='price_now',
            field=models.CharField(default='$', max_length=100),
        ),
    ]
