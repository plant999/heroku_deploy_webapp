# Generated by Django 3.0.6 on 2020-05-18 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EoResults',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_arr', models.CharField(max_length=4000)),
                ('result1', models.IntegerField()),
                ('result2', models.IntegerField()),
            ],
            options={
                'db_table': 'eo_results',
            },
        ),
    ]
