# Generated by Django 3.1.6 on 2021-03-10 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('managment', '0011_auto_20210228_0722'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_all',
            name='branch',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='student_all',
            name='enrollment_number',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='student_all',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]