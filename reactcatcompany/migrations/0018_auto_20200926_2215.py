# Generated by Django 3.1.1 on 2020-09-26 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reactcatcompany', '0017_auto_20200926_0444'),
    ]

    operations = [
        migrations.AddField(
            model_name='pythoncourse',
            name='contactdetails',
            field=models.TextField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='pythoncourse',
            name='coursestart',
            field=models.CharField(max_length=255, null=True),
        ),
    ]