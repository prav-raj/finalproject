# Generated by Django 5.0.4 on 2024-04-26 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NbaTeam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(max_length=50)),
                ('founded_year', models.IntegerField()),
                ('championships_won', models.IntegerField()),
            ],
        ),
    ]
