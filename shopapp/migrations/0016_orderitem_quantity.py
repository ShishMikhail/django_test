# Generated by Django 4.1.4 on 2023-05-29 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopapp', '0015_remove_orderitem_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='quantity',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
