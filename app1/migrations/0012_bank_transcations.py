# Generated by Django 4.1 on 2023-02-08 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0011_delete_bank_transcations'),
    ]

    operations = [
        migrations.CreateModel(
            name='bank_transcations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank_account', models.CharField(blank=True, max_length=255, null=True)),
                ('transcation_type', models.CharField(blank=True, max_length=255, null=True)),
                ('instno', models.IntegerField(blank=True, null=True)),
                ('instdate', models.DateField(blank=True, null=True)),
                ('amount', models.IntegerField(blank=True, null=True)),
                ('acnum', models.CharField(blank=True, max_length=255, null=True)),
                ('ifscode', models.CharField(blank=True, max_length=255, null=True)),
                ('bank_name', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]