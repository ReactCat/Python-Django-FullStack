# Generated by Django 3.1.1 on 2020-09-25 04:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reactcatcompany', '0015_auto_20200925_0444'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pythoncourse',
            old_name='coursenumber',
            new_name='coursecode',
        ),
    ]
