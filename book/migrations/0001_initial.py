# Generated by Django 3.1.2 on 2020-10-21 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=100)),
                ('publishing_company', models.CharField(default='', max_length=50)),
                ('edition', models.IntegerField()),
                ('year_publication', models.CharField(default='', max_length=4)),
                ('status', models.CharField(choices=[('B', 'borrowed'), ('A', 'available')], max_length=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
