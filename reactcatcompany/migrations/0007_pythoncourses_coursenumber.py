# Generated by Django 3.1.1 on 2020-09-24 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reactcatcompany', '0006_auto_20200924_2141'),
    ]

    operations = [
        migrations.AddField(
            model_name='pythoncourses',
            name='coursenumber',
            field=models.TextField(default=False),
        ),
    ]
