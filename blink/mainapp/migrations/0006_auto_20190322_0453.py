# Generated by Django 2.1.4 on 2019-03-22 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_auto_20190322_0448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='project_cover',
            field=models.ImageField(upload_to='media'),
        ),
    ]