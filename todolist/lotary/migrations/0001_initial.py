# Generated by Django 5.0.6 on 2024-07-09 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Wins',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=512)),
                ('surname', models.CharField(max_length=512)),
                ('summa_of_wins', models.CharField(max_length=512)),
            ],
        ),
    ]
