# Generated by Django 5.1.4 on 2025-01-15 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LoanScenario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purchase_price', models.FloatField()),
                ('down_payment', models.FloatField()),
                ('down_payment_type', models.CharField(choices=[('percent', 'Percent'), ('dollar', 'Dollar')], max_length=10)),
                ('mortgage_term', models.IntegerField()),
                ('term_unit', models.CharField(choices=[('years', 'Years'), ('months', 'Months')], max_length=10)),
                ('interest_rate', models.FloatField()),
                ('monthly_payment', models.FloatField()),
                ('annual_payment', models.FloatField()),
                ('total_payment', models.FloatField()),
                ('total_interest', models.FloatField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
