# Generated by Django 4.1.2 on 2022-11-03 14:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_data_alamat'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='waktu',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
