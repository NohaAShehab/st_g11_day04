# Generated by Django 3.2.7 on 2021-09-07 08:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('depts', '0001_initial'),
        ('students', '0003_auto_20210907_0956'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='dept',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='depts.department'),
            preserve_default=False,
        ),
    ]
