# Generated by Django 5.1.3 on 2024-12-01 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pharmacy', '0003_remove_medication_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='prescription',
            name='address',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='prescription',
            name='allergies',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='prescription',
            name='city',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='prescription',
            name='conditions',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='prescription',
            name='directions',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='prescription',
            name='drug_code',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='prescription',
            name='drug_quantity',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='prescription',
            name='state',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='prescription',
            name='third_party_code',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]