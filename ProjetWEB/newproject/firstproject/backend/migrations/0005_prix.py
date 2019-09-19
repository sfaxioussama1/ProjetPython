# Generated by Django 2.2 on 2019-05-04 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_department'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prix',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=20)),
                ('prix', models.FloatField()),
                ('service1', models.CharField(blank=True, max_length=10, null=True)),
                ('service2', models.CharField(blank=True, max_length=10, null=True)),
                ('service3', models.CharField(blank=True, max_length=10, null=True)),
                ('service4', models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
    ]
