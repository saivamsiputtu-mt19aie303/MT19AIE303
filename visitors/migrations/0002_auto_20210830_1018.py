# Generated by Django 3.2.6 on 2021-08-30 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visitors', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitor',
            name='age',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='visitor',
            name='fname',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='visitor',
            name='lname',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterModelTable(
            name='visitor',
            table='visitors',
        ),
    ]
