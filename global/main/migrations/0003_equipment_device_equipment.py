# Generated by Django 4.1.3 on 2022-11-30 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_category_alter_device_options_device_category_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='device',
            name='equipment',
            field=models.CharField(default='Смартфон', max_length=100),
        ),
    ]