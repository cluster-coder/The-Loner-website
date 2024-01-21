# Generated by Django 4.2.7 on 2024-01-20 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theloner', '0011_rename_insertedinto_additionalpagehtml_pages_inserted'),
    ]

    operations = [
        migrations.RenameField(
            model_name='additionalpagehtml',
            old_name='pages_inserted',
            new_name='pages_adding_me',
        ),
        migrations.RemoveField(
            model_name='additionaloptionhtml',
            name='insertedInto',
        ),
        migrations.AddField(
            model_name='additionaloptionhtml',
            name='options_adding_me',
            field=models.ManyToManyField(to='theloner.secreturl'),
        ),
    ]