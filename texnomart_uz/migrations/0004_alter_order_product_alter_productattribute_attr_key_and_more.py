# Generated by Django 5.0.7 on 2024-10-16 09:06

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('texnomart_uz', '0003_alter_comment_user_alter_order_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='product',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='texnomart_uz.product'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='productattribute',
            name='attr_key',
            field=models.ForeignKey(blank=True, default=2, on_delete=django.db.models.deletion.CASCADE, to='texnomart_uz.attributekey'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='productattribute',
            name='attr_value',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='texnomart_uz.attributevalue'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='productattribute',
            name='product',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, related_name='attributes', to='texnomart_uz.product'),
            preserve_default=False,
        )
    ]
