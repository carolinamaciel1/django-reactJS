# Generated by Django 3.0.5 on 2020-05-02 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saints', '0002_auto_20200502_0139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='saints',
            name='id',
            field=models.IntegerField(auto_created=True, primary_key=True, serialize=False),
        ),
    ]
