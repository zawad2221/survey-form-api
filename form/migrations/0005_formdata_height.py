# Generated by Django 3.1.3 on 2020-11-22 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0004_auto_20201122_1442'),
    ]

    operations = [
        migrations.AddField(
            model_name='formdata',
            name='height',
            field=models.CharField(default=0, max_length=11),
            preserve_default=False,
        ),
    ]
