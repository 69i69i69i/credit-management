# Generated by Django 2.1 on 2020-07-25 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=40)),
                ('pan', models.CharField(default='', max_length=30)),
                ('phone', models.CharField(default='', max_length=20)),
                ('current_credit', models.IntegerField()),
            ],
        ),
    ]
