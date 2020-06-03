# Generated by Django 2.2.5 on 2020-06-01 07:49

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('Gid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('Oid', models.AutoField(primary_key=True, serialize=False)),
                ('list_Order', models.CharField(max_length=300)),
                ('sum_Order', models.CharField(max_length=300)),
                ('point', models.IntegerField()),
                ('sum_price', models.IntegerField()),
                ('created_at', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('Pid', models.AutoField(primary_key=True, serialize=False)),
                ('P_name', models.CharField(max_length=1000)),
                ('P_nameEng', models.CharField(max_length=1000)),
                ('price', models.CharField(max_length=300)),
                ('p_type', models.CharField(blank=True, choices=[('HOT', 'hot'), ('COLD', 'cold'), ('BLENDED', 'blended')], max_length=10, null=True)),
                ('created_at', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(blank=True, max_length=30)),
                ('birthdate', models.DateField(blank=True, null=True)),
                ('role', models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Supervisor'), (2, 'Employees')], null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Incustumer',
            fields=[
                ('face_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=300)),
                ('last_name', models.CharField(max_length=300)),
                ('phone', models.CharField(max_length=20)),
                ('age', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254, null=True, unique=True)),
                ('career', models.CharField(max_length=300)),
                ('imageInfo', models.ImageField(blank=True, null=True, upload_to='images/Incustumer/')),
                ('imageInfo2', models.ImageField(blank=True, null=True, upload_to='images/Incustumer/')),
                ('gender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Webcashier.Gender')),
            ],
        ),
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(default='', max_length=300)),
                ('first_name', models.CharField(max_length=300)),
                ('last_name', models.CharField(max_length=300)),
                ('dob', models.DateField(default=django.utils.timezone.now)),
                ('age', models.CharField(max_length=20)),
                ('gen_der', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='Webcashier.Gender')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]