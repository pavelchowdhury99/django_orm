# Generated by Django 4.1.5 on 2023-01-31 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TestTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('int_field', models.IntegerField(default=0)),
                ('char_field', models.CharField(max_length=200)),
                ('date_field', models.DateField()),
                ('date_time_field', models.DateTimeField()),
            ],
        ),
    ]
