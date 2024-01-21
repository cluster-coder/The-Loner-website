# Generated by Django 4.2.7 on 2023-12-24 22:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SecretUrl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('secretWord', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='choices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tellstoryClass', models.CharField(max_length=2000)),
                ('tellstoryText', models.TextField()),
                ('wolfClass', models.CharField(max_length=2000)),
                ('wolfText', models.CharField(max_length=2000)),
                ('iconClass', models.CharField(max_length=2000)),
                ('iconSrc', models.CharField(max_length=800)),
                ('headerClass', models.CharField(max_length=2000)),
                ('headerCssUrl', models.CharField(max_length=800)),
                ('position', models.PositiveSmallIntegerField()),
                ('urlBearer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='theloner.secreturl')),
            ],
        ),
    ]
