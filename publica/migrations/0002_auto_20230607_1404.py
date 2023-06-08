# Generated by Django 3.2.18 on 2023-06-07 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publica', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('asunto', models.CharField(max_length=50)),
                ('mensaje', models.TextField(max_length=500)),
                ('tipo_consulta', models.IntegerField(choices=[(1, 'Oferta del día'), (2, 'Comprar en cantidad'), (3, 'Oferta para compartir')])),
                ('suscripcion', models.BooleanField(default=False)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
            ],
        )]