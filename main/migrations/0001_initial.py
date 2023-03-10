# Generated by Django 4.1.7 on 2023-02-22 13:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.menu')),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='children', to='main.menuitem')),
            ],
        ),
    ]
