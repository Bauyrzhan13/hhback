# Generated by Django 2.1.5 on 2021-04-15 20:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20210415_2006'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacancy',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Company'),
        ),
    ]




