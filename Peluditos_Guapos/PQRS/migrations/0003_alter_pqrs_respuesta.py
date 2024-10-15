

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PQRS', '0002_pqrs_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pqrs',
            name='Respuesta',
            field=models.TextField(max_length=500),
        ),
    ]
