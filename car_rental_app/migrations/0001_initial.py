# Generated by Django 3.0.5 on 2020-10-26 20:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('car_id', models.IntegerField(primary_key=True, serialize=False)),
                ('model', models.CharField(max_length=45, null=True)),
                ('brand', models.CharField(max_length=45, null=True)),
                ('color', models.CharField(max_length=45, null=True)),
                ('description', models.CharField(max_length=500, null=True)),
                ('date_of_purchase', models.DateField(null=True, verbose_name='Date of purchase')),
                ('time_of_purchase', models.TimeField(null=True, verbose_name='Time of purchase')),
                ('available', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customer_id', models.IntegerField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=45, null=True)),
                ('last_name', models.CharField(max_length=45, null=True)),
                ('mobile_no', models.BigIntegerField()),
                ('car_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car_rental_app.Car')),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('booking_id', models.IntegerField(primary_key=True, serialize=False)),
                ('date_of_issue', models.DateTimeField(verbose_name='Date of Issue')),
                ('date_of_return', models.DateTimeField(verbose_name='Date of Return')),
                ('pickup_location', models.CharField(max_length=500)),
                ('car_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car_rental_app.Car')),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car_rental_app.Customer')),
            ],
        ),
    ]
