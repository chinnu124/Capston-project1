# Generated by Django 2.1.5 on 2019-03-10 06:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tinker', '0002_auto_20190310_1146'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendee',
            name='event',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='tinker.Event'),
            preserve_default=False,
        ),
    ]
