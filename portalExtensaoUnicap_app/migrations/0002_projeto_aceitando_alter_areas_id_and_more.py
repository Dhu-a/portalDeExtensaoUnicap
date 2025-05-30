# Generated by Django 5.1.1 on 2025-04-28 17:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portalExtensaoUnicap_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='projeto',
            name='aceitando',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='areas',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='areas',
            name='id_projeto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='areas', to='portalExtensaoUnicap_app.projeto'),
        ),
        migrations.AlterField(
            model_name='dias',
            name='dia',
            field=models.TextField(max_length=13),
        ),
        migrations.AlterField(
            model_name='dias',
            name='turno',
            field=models.TextField(max_length=5),
        ),
    ]
