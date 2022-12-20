# Generated by Django 4.1.3 on 2022-11-28 14:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('year', models.CharField(max_length=20)),
                ('country', models.CharField(max_length=100)),
                ('camera', models.CharField(max_length=10)),
                ('dynamic', models.CharField(max_length=255)),
                ('display', models.CharField(max_length=255)),
                ('ram', models.CharField(max_length=255)),
                ('memory', models.CharField(max_length=255)),
                ('text', models.TextField(max_length=255)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]