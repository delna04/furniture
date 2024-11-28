# Generated by Django 5.1.2 on 2024-11-14 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FurApp', '0005_rename_mrp_cartdb_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='orderdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=100, null=True)),
                ('Place', models.CharField(blank=True, max_length=100, null=True)),
                ('Email', models.CharField(blank=True, max_length=100, null=True)),
                ('Address', models.CharField(blank=True, max_length=100, null=True)),
                ('Phone_Number', models.IntegerField(blank=True, null=True)),
                ('Message', models.CharField(blank=True, max_length=100, null=True)),
                ('Total_Price', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
