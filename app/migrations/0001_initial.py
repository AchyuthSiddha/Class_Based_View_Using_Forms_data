# Generated by Django 4.1.4 on 2023-05-15 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('sid', models.IntegerField()),
                ('sname', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254)),
                ('sage', models.IntegerField()),
            ],
        ),
    ]
