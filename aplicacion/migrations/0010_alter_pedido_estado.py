# Generated by Django 5.0.6 on 2024-06-30 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0009_pedido_estado_delete_detallepedido'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='estado',
            field=models.CharField(choices=[('En Proceso', 'En Proceso'), ('Finalizado', 'Finalizado')], default='En Proceso', max_length=10),
        ),
    ]