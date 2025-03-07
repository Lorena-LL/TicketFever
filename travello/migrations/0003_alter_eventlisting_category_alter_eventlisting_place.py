# Generated by Django 5.1.3 on 2024-12-31 18:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0002_place_remove_eventlisting_organiser_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventlisting',
            name='category',
            field=models.CharField(choices=[('concert', 'Concert'), ('opera', 'Opera'), ('theater', 'Piesa de Teatru'), ('standup', 'Stand-Up Comedy'), ('ballet', 'Balet')], max_length=100),
        ),
        migrations.AlterField(
            model_name='eventlisting',
            name='place',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travello.place'),
        ),
    ]
