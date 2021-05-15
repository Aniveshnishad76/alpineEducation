# Generated by Django 3.1.6 on 2021-02-23 03:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('managment', '0005_auto_20210219_1102'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserOTP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_set', models.DateTimeField(auto_now=True)),
                ('otp', models.CharField(max_length=5)),
                ('enrollment_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='managment.student_register')),
            ],
        ),
    ]