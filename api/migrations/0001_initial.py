# Generated by Django 5.0.6 on 2024-05-20 02:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('url', models.CharField(max_length=255)),
                ('is_filtered', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_insertion', models.DateField(auto_now_add=True)),
                ('lu', models.BooleanField(default=False)),
                ('title', models.CharField(max_length=255)),
                ('url', models.CharField(max_length=255)),
                ('location', models.CharField(blank=True, max_length=255, null=True)),
                ('date_publication', models.DateField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('job_id', models.CharField(blank=True, max_length=255, null=True)),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='offres', to='api.site')),
            ],
        ),
    ]
