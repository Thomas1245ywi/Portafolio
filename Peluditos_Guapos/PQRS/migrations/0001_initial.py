
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Estado_pqrs', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'Estado_pqrs',
                'verbose_name_plural': 'Estado pqrs',
                'db_table': 'pqrs_estado',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Tipo_pqrs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tipo_pqrs', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'Tipo pqrs',
                'verbose_name_plural': 'Tipos pqrs',
                'db_table': 'tipo_pqrs',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='PQRS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now=True, db_comment='Fecha de creacion', verbose_name='Fecha de creacion')),
                ('correo', models.CharField(blank=True, max_length=100, null=True, verbose_name='correo electronico')),
                ('descripcion', models.TextField(max_length=500, verbose_name='Descripcion')),
                ('Respuesta', models.CharField(max_length=150)),
                ('Estado', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='PQRS.estado')),
                ('Tipo_pqrs', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PQRS.tipo_pqrs')),
            ],
            options={
                'verbose_name': 'PQRS',
                'verbose_name_plural': 'PQRS',
                'db_table': 'pqrs',
                'ordering': ['id'],
            },
        ),
    ]
