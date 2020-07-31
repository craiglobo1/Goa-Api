# Generated by Django 3.0.2 on 2020-07-30 17:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='buisness',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Api.Buisness'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='buisness',
            name='owner',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='Api.Owner'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='taxes',
            name='buisness',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='Api.Buisness'),
            preserve_default=False,
        ),
    ]
