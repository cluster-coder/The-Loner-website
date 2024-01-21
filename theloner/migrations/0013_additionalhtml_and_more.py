# Generated by Django 4.2.7 on 2024-01-20 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theloner', '0012_rename_pages_inserted_additionalpagehtml_pages_adding_me_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='additionalHtml',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tagType', models.CharField(choices=[('div', 'div'), ('pre', 'pre'), ('img', 'img'), ('pre', 'pre'), ('p', 'p'), ('h1', 'h1'), ('h2', 'h2'), ('h3', 'h3'), ('h4', 'h4'), ('h5', 'h5'), ('h6', 'h6')], max_length=100)),
                ('tagClasses', models.CharField(blank=True, max_length=2000)),
                ('contentInside', models.TextField(blank=True)),
                ('insertBefore', models.IntegerField(choices=[(0, 'header'), (1, 'wolf'), (2, 'choices'), (3, 'tellstory'), (4, 'beyond')])),
                ('options_adding_me', models.ManyToManyField(blank=True, to='theloner.choices')),
                ('pages_adding_me', models.ManyToManyField(blank=True, to='theloner.secreturl')),
            ],
        ),
        migrations.RemoveField(
            model_name='additionalpagehtml',
            name='pages_adding_me',
        ),
        migrations.DeleteModel(
            name='additionalOptionHtml',
        ),
        migrations.DeleteModel(
            name='additionalPageHtml',
        ),
    ]