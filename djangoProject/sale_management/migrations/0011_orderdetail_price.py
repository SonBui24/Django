# Generated by Django 4.0.3 on 2022-05-06 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sale_management', '0010_customer_created_at_customer_created_by_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderdetail',
            name='price',
            field=models.BigIntegerField(default=0),
            preserve_default=False,
        ),
    ]
