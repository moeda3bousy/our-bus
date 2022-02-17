# Generated by Django 4.0.2 on 2022-02-16 17:53

import creditcards.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='available',
            name='to2',
            field=models.CharField(choices=[('Aswan', 'Aswan'), ('Alexandria', 'Alexandria'), ('Hurghada', 'Hurghada'), ('North coast', 'North coast'), ('Dahab', 'Dahab'), ('Sharm El-Sheikh', 'Sharm El-Sheikh')], max_length=20, null='True', verbose_name='to '),
        ),
        migrations.AlterField(
            model_name='ride',
            name='card_number',
            field=creditcards.models.CardNumberField(blank=True, max_length=19, null='True', verbose_name='Card Number'),
        ),
        migrations.AlterField(
            model_name='ride',
            name='expiry_date',
            field=creditcards.models.CardExpiryField(null='True', verbose_name='Expiry Date'),
        ),
        migrations.AlterField(
            model_name='ride',
            name='to',
            field=models.CharField(choices=[('Aswan', 'Aswan'), ('Alexandria', 'Alexandria'), ('Hurghada', 'Hurghada'), ('North coast', 'North coast'), ('Dahab', 'Dahab'), ('Sharm El-Sheikh', 'Sharm El-Sheikh')], max_length=20, null='True', verbose_name='To'),
        ),
    ]
