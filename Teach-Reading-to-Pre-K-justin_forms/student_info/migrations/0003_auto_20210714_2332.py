# Generated by Django 3.2.4 on 2021-07-15 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_info', '0002_alter_classroom_average_at_risk'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classroom',
            name='grade',
            field=models.CharField(max_length=4),
        ),
        migrations.AlterField(
            model_name='student',
            name='grade',
            field=models.CharField(max_length=4),
        ),
    ]
