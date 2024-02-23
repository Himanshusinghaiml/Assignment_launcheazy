# Generated by Django 5.0.2 on 2024-02-23 17:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UMS', '0002_alter_organization_billing_group_billinggroup_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='billinggroup',
            name='organization',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='billing_group_information', to='UMS.organization'),
        ),
    ]