# Generated by Django 2.2.5 on 2020-06-04 13:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Webcashier', '0003_auto_20200604_1626'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='Webcashier.Incustumer'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='Emp',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
