# Generated by Django 3.1.6 on 2021-02-28 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('managment', '0008_otp'),
    ]

    operations = [
        migrations.AddField(
            model_name='student_all',
            name='previous_panding',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='student_all',
            name='semester_fees',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='student_all',
            name='total_panding',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]