# Generated by Django 5.1.5 on 2025-01-24 11:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_order_node_alter_product_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='node',
            new_name='note',
        ),
    ]
