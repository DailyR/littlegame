# Generated by Django 2.1.4 on 2019-02-26 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dbcontrol', '0003_auto_20190225_1137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
