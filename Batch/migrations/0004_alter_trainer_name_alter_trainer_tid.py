# Generated by Django 4.1.5 on 2023-02-03 05:55

import Batch.validators
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Batch', '0003_batchdb'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainer',
            name='name',
            field=models.CharField(max_length=40, validators=[Batch.validators.Minchar, django.core.validators.MaxLengthValidator(20)]),
        ),
        migrations.AlterField(
            model_name='trainer',
            name='tid',
            field=models.CharField(max_length=10, primary_key=True, serialize=False, validators=[Batch.validators.Minchar]),
        ),
    ]
