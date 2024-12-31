# Generated by Django 5.1.3 on 2024-11-17 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EventListing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('category', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('price', models.FloatField()),
                ('total_nr_tickets', models.IntegerField()),
                ('available_nr_tickets', models.IntegerField()),
                ('organiser_id', models.IntegerField()),
                ('place_id', models.IntegerField()),
                ('img', models.ImageField(upload_to='pics')),
            ],
        ),
    ]
