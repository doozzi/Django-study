# Generated by Django 3.2.18 on 2023-04-13 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('bid', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('author', models.CharField(max_length=50)),
                ('category', models.CharField(max_length=50)),
                ('pages', models.IntegerField()),
                ('price', models.IntegerField()),
                ('published_date', models.DateField()),
                ('description', models.TextField()),
            ],
        ),
    ]
