# Generated by Django 5.0.6 on 2024-06-20 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_alter_catalogue_id_alter_chambre_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='Adulte',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='Note',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='Phone',
            field=models.IntegerField(),
        ),
    ]
