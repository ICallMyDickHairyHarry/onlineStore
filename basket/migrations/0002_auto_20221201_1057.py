# Generated by Django 3.2.16 on 2022-12-01 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basket', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='ord_status',
            field=models.CharField(default='1', max_length=1),
        ),
        migrations.AlterField(
            model_name='order',
            name='pay_date',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
    ]