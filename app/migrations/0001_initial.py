# Generated by Django 4.1.7 on 2023-05-23 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('principal', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
            ],
        ),
    ]
