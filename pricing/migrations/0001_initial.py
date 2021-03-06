# Generated by Django 3.1.2 on 2020-10-23 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pricing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('penalty', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True)),
                ('interest_per_day', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True)),
                ('delayed_days', models.CharField(default='', max_length=50)),
            ],
        ),
    ]
