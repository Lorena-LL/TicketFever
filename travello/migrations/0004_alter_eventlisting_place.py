# Generated by Django 5.1.3 on 2024-12-31 18:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0003_alter_eventlisting_category_alter_eventlisting_place'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventlisting',
            name='place',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='travello.place'),
        ),
    ]
