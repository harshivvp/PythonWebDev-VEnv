# Generated by Django 2.0.2 on 2018-02-07 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecomapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('food', 'Food'), ('misc', 'Miscellaneous'), ('daily', 'Daily'), ('basic', 'Basic'), ('unk', 'Unknown')], default='food', max_length=50),
        ),
    ]
