# Generated by Django 5.1 on 2024-09-25 14:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('arts', '0011_rename_count_student_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='Count',
        ),
    ]
