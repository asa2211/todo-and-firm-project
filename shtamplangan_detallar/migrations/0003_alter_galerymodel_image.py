# Generated by Django 5.0 on 2024-01-06 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shtamplangan_detallar', '0002_alter_galerymodel_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='galerymodel',
            name='image',
            field=models.ImageField(null=True, upload_to='photo'),
        ),
    ]