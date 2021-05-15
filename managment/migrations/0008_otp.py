# Generated by Django 3.1.6 on 2021-02-24 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('managment', '0007_faculty_faculty_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Otp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enrollment_number', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=30)),
                ('otp', models.CharField(max_length=5)),
                ('status', models.CharField(default='Vaild', max_length=20)),
            ],
        ),
    ]