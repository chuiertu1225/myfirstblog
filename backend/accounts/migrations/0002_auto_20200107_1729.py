# Generated by Django 2.2.8 on 2020-01-07 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='age',
            field=models.IntegerField(blank=True, default=18, verbose_name='年龄'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='uuid',
            field=models.CharField(default='VTdvYNUZYro4CZvZfeTKFg', editable=False, max_length=22, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
