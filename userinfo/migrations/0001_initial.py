# Generated by Django 2.0.3 on 2019-04-01 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user_information',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('openid', models.CharField(max_length=30)),
                ('nickname', models.CharField(max_length=20, null=True)),
                ('gender', models.IntegerField(null=True)),
                ('city', models.CharField(max_length=20, null=True)),
                ('province', models.CharField(max_length=20, null=True)),
                ('country', models.CharField(max_length=20, null=True)),
                ('portrait', models.URLField(null=True)),
            ],
        ),
    ]
