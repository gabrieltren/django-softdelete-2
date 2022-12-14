# Generated by Django 4.1 on 2022-08-08 22:47

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movimentacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('deleted_at', models.DateTimeField(blank=True, null=True, verbose_name='Deletado em ')),
                ('valor', models.DecimalField(decimal_places=2, default=0.0, max_digits=15)),
                ('data', models.DateTimeField(blank=True, null=True)),
                ('tipo', models.CharField(choices=[('entrada', 'Entrada'), ('saida', 'Saida')], max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
