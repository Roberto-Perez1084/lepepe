# Generated by Django 5.1 on 2024-11-22 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id_cliente', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('nom_cliente', models.CharField(max_length=15)),
                ('apelli_cliente', models.CharField(max_length=15)),
                ('edad_cliente', models.CharField(max_length=2)),
                ('tel_cliente', models.CharField(max_length=13)),
                ('email_cliente', models.CharField(max_length=50)),
                ('fech_reg', models.DateField()),
            ],
        ),
    ]