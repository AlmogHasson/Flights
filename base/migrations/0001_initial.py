# Generated by Django 3.2.8 on 2022-07-16 14:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Airline_Companie',
            fields=[
                ('_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Countrie',
            fields=[
                ('name', models.CharField(max_length=50, unique=True)),
                ('_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('f_name', models.CharField(max_length=50)),
                ('l_name', models.CharField(max_length=50)),
                ('address', models.TextField()),
                ('Phone_No', models.CharField(max_length=12)),
                ('Credit_Card', models.DateTimeField(max_length=16)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('departure', models.DateTimeField()),
                ('landing_time', models.DateTimeField()),
                ('airline_company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.airline_companie')),
                ('destination_country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dest_id', to='base.countrie')),
                ('origin_country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.countrie')),
            ],
        ),
        migrations.CreateModel(
            name='User_Role',
            fields=[
                ('_id', models.IntegerField(primary_key=True, serialize=False)),
                ('role_name', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer_id', to='base.customer')),
                ('flight', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.flight')),
            ],
        ),
        migrations.AddField(
            model_name='airline_companie',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.countrie'),
        ),
        migrations.AddField(
            model_name='airline_companie',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('_id', models.IntegerField(primary_key=True, serialize=False)),
                ('f_name', models.CharField(max_length=50)),
                ('l_name', models.CharField(max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]