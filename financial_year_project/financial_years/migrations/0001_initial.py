# Generated by Django 5.2.2 on 2025-06-08 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FinancialYear',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='e.g., FY 2023-24', max_length=100, unique=True)),
                ('start_date', models.DateField(unique=True)),
                ('end_date', models.DateField(unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Financial Year',
                'verbose_name_plural': 'Financial Years',
                'ordering': ['-start_date'],
            },
        ),
    ]
