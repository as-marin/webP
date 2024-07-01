# Generated by Django 5.0.6 on 2024-06-30 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0008_detallepedido'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='estado',
            field=models.CharField(choices=[('EP', 'En Proceso'), ('F', 'Finalizado')], default='EP', max_length=2),
        ),
        migrations.DeleteModel(
            name='DetallePedido',
        ),
    ]