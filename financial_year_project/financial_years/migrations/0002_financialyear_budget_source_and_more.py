# Generated by Django 5.2.2 on 2025-06-10 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('financial_years', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='financialyear',
            name='budget_source',
            field=models.CharField(choices=[('COMMITTED', 'Committed'), ('DPIP', 'Dpip')], default='DPIP', help_text='Select the budget source.', max_length=10),
        ),
        migrations.AlterField(
            model_name='financialyear',
            name='end_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='financialyear',
            name='name',
            field=models.CharField(help_text='e.g., FY 2025-2026', max_length=9, unique=True),
        ),
        migrations.AlterField(
            model_name='financialyear',
            name='start_date',
            field=models.DateField(),
        ),
    ]
