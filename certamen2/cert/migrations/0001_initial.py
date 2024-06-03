# Generated by Django 4.2.13 on 2024-06-03 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('tema', models.CharField(max_length=100)),
                ('patrocinado', models.BooleanField(default=False)),
            ],
        ),
    ]
