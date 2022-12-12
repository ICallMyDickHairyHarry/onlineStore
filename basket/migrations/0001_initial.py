# Generated by Django 3.2.16 on 2022-12-01 06:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('catalogue', '0005_auto_20221128_1453'),
        ('registration', '0003_adm'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ord_status', models.CharField(max_length=1)),
                ('cr_date', models.DateTimeField()),
                ('pay_date', models.DateTimeField()),
                ('full_pr', models.PositiveSmallIntegerField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.customer')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.adm')),
            ],
        ),
        migrations.CreateModel(
            name='Prod_list',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pr_amount', models.PositiveSmallIntegerField()),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='basket.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogue.product')),
            ],
        ),
    ]