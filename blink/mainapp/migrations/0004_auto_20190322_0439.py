# Generated by Django 2.1.4 on 2019-03-22 11:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_auto_20190319_0430'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='project_title_bg',
            new_name='project_cover',
        ),
    ]
