# Generated by Django 4.2.6 on 2023-11-28 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venda', '0005_alter_carro_cambio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carro',
            name='cambio',
            field=models.CharField(choices=[('Manual', 'Manual'), ('Automático', 'Automático')], default='Manual', max_length=100, verbose_name='Câmbio'),
        ),
    ]