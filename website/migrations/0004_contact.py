# Generated by Django 4.1 on 2022-08-20 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_portfolio'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=50)),
            ],
        ),
    ]
