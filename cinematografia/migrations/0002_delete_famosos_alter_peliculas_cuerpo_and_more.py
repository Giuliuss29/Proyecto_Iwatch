# Generated by Django 5.0.6 on 2024-07-01 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinematografia', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Famosos',
        ),
        migrations.AlterField(
            model_name='peliculas',
            name='cuerpo',
            field=models.CharField(max_length=9000),
        ),
        migrations.AlterField(
            model_name='peliculas',
            name='img',
            field=models.ImageField(null=True, upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='series',
            name='cuerpo',
            field=models.CharField(max_length=9000),
        ),
        migrations.AlterField(
            model_name='series',
            name='img',
            field=models.ImageField(null=True, upload_to='media/'),
        ),
    ]
