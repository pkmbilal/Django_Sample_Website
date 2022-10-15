# Generated by Django 4.1 on 2022-08-21 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=50)),
                ('message', models.TextField()),
            ],
        ),
    ]
