# Generated by Django 4.1 on 2022-09-29 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0019_alter_order_payment'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderproduct',
            name='offer_price',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
    ]
