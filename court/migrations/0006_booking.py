# Generated by Django 3.2.2 on 2022-07-11 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('court', '0005_auto_20220710_1937'),
    ]

    operations = [
        migrations.CreateModel(
            name='booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(default='1')),
                ('court_id', models.IntegerField(default='1')),
                ('hour', models.IntegerField(default='1')),
                ('date', models.DateField()),
            ],
        ),
    ]
