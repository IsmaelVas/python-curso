# Generated by Django 5.0.6 on 2024-06-26 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interno', '0007_rename_cidades_cidade'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='imagem',
            field=models.ImageField(null=True, upload_to='produtos_imagem'),
        ),
    ]