# Generated by Django 5.1.5 on 2025-01-24 12:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_rename_node_order_note'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='note',
        ),
    ]
