# Generated by Django 3.0.7 on 2020-07-03 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='destination',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.TextField()),
                ('img', models.ImageField(upload_to='pics')),
            ],
        ),
    ]