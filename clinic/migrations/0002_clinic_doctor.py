# Generated by Django 3.2 on 2021-04-12 14:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clinic', '0001_initial'),
        ('doctor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='clinic',
            name='doctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctor.doctor'),
        ),
    ]
