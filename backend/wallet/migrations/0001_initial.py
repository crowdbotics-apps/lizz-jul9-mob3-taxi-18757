# Generated by Django 2.2.14 on 2020-07-09 17:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taxi_profile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserWallet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.FloatField()),
                ('expiration_date', models.DateTimeField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='userwallet_user', to='taxi_profile.UserProfile')),
            ],
        ),
        migrations.CreateModel(
            name='PaymentMethod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_token', models.CharField(max_length=255)),
                ('payment_account', models.CharField(max_length=10)),
                ('timestamp_created', models.DateTimeField(auto_now_add=True)),
                ('wallet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='paymentmethod_wallet', to='wallet.UserWallet')),
            ],
        ),
        migrations.CreateModel(
            name='DriverWallet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.FloatField()),
                ('expiration_date', models.DateTimeField()),
                ('driver', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='driverwallet_driver', to='taxi_profile.DriverProfile')),
            ],
        ),
    ]
