# Generated by Django 4.2.6 on 2023-10-28 02:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data_sources', '0004_alter_company_companyofficers'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='companyOfficers',
        ),
    ]