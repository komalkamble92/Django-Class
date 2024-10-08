# Generated by Django 5.1 on 2024-09-18 14:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arts', '0007_remove_salary_record_salary1_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='SalaryRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date_paid', models.DateField()),
                ('notes', models.TextField(blank=True, null=True)),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='salary_records', to='arts.teacher')),
            ],
        ),
    ]
