# Generated by Django 2.1.4 on 2019-02-25 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dbcontrol', '0002_auto_20190109_2008'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='link',
            name='id',
        ),
        migrations.AddField(
            model_name='link',
            name='_id',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
        ),
    ]