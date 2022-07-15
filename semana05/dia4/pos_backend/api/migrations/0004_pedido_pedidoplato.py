# Generated by Django 3.2 on 2022-07-15 00:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0003_plato'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('pedido_id', models.AutoField(primary_key=True, serialize=False)),
                ('pedido_fech', models.DateTimeField(null=True, verbose_name='Fecha')),
                ('pedido_nro', models.CharField(default='', max_length=100, verbose_name='Nro Pedido')),
                ('pedido_est', models.CharField(choices=[('solicitado', 'Solicitado'), ('entregado', 'entregado')], default='solicitado', max_length=100, verbose_name='Estado')),
                ('mesa_id', models.ForeignKey(db_column='mesa_id', on_delete=django.db.models.deletion.RESTRICT, to='api.mesa', verbose_name='Nro Mesa')),
                ('usu_id', models.ForeignKey(db_column='usu_id', on_delete=django.db.models.deletion.RESTRICT, related_name='Pedidos', to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
            options={
                'db_table': 'tbl_pedido',
            },
        ),
        migrations.CreateModel(
            name='PedidoPlato',
            fields=[
                ('pedidoplato_id', models.AutoField(primary_key=True, serialize=False)),
                ('pedidoplato_cant', models.IntegerField(default=1, verbose_name='Cantidad')),
                ('pedido_id', models.ForeignKey(db_column='pedido_id', on_delete=django.db.models.deletion.RESTRICT, related_name='pedidoplatos', to='api.pedido', verbose_name='Pedido')),
                ('plato_id', models.ForeignKey(db_column='plato_id', on_delete=django.db.models.deletion.RESTRICT, related_name='pedidoplatos', to='api.plato', verbose_name='Plato')),
            ],
            options={
                'db_table': 'tbl_pedido_plato',
            },
        ),
    ]
