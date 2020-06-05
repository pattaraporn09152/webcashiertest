# Generated by Django 2.2.5 on 2020-06-04 08:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Webcashier', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='Emp',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Webcashier.Employees'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='incustumer',
            name='face_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]