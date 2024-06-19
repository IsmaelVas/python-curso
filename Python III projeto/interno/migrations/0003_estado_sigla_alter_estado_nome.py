# Generated by Django 5.0.6 on 2024-06-19 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interno', '0002_estado'),
    ]

    operations = [
        migrations.AddField(
            model_name='estado',
            name='sigla',
            field=models.CharField(default='sc', max_length=2),
        ),
        migrations.AlterField(
            model_name='estado',
            name='nome',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
