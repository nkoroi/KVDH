# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-04-21 17:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vdh', '0020_auto_20170420_1748'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClinicalWorkData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(help_text='Please use the following format: <em>MM-DD-YYYY</em>.')),
                ('animal_species', models.CharField(max_length=100)),
                ('identification', models.CharField(max_length=100)),
                ('owner', models.CharField(max_length=100)),
                ('complaint', models.CharField(max_length=1000)),
                ('diagnosis', models.CharField(max_length=1000)),
                ('diagnostic_method_used', models.CharField(choices=[('TENT', 'Tentative'), ('LAB', 'Lab'), ('SURG', 'Surgical'), ('PHY', 'Physical exam eg, Palpation')], max_length=100)),
                ('treatment_product_used', models.CharField(max_length=100)),
                ('treatment_amount_used', models.CharField(max_length=100)),
                ('treatment_batch_no', models.IntegerField(max_length=20, unique=True)),
                ('outcome_of_treatment', models.CharField(max_length=500)),
                ('advice_given', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='PracticeData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('CW', 'Clinical work/ Herd health/ Extension service'), ('VMP', 'Vetenary medicine production'), ('VMD', 'Vetenary medicine distribution')], max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SupervisingVet',
            fields=[
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('kvb_reg_no', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('email', models.EmailField(max_length=254)),
                ('academic_inst', models.CharField(max_length=100)),
                ('program_studied', models.CharField(choices=[('CERT', 'Certificate in AH'), ('DIP', 'Diploma in AH'), ('BSC', 'Bachelor of Science in AH'), ('BVM', 'Bachelor of Science in Vetenary Medicine')], max_length=100)),
                ('index_no', models.IntegerField(unique=True)),
                ('year_of_graduation', models.DateField(help_text='Please use the following format: <em>MM-DD-YYYY</em>.')),
                ('academic_cert_reg_no', models.IntegerField(unique=True)),
                ('any_other_certs', models.CharField(max_length=500)),
                ('license_no', models.IntegerField(unique=True)),
                ('license_exp_date', models.DateField(help_text='Please use the following format: <em>MM-DD-YYYY</em>.')),
                ('current_station_of_work', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='VetMedicineDistributer',
            fields=[
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('kvb_reg_no', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('email', models.EmailField(max_length=254)),
                ('academic_inst', models.CharField(max_length=100)),
                ('program_studied', models.CharField(choices=[('CERT', 'Certificate in AH'), ('DIP', 'Diploma in AH'), ('BSC', 'Bachelor of Science in AH'), ('BVM', 'Bachelor of Science in Vetenary Medicine')], max_length=100)),
                ('index_no', models.IntegerField(unique=True)),
                ('year_of_graduation', models.DateField(help_text='Please use the following format: <em>MM-DD-YYYY</em>.')),
                ('academic_cert_reg_no', models.IntegerField(unique=True)),
                ('any_other_certs', models.CharField(max_length=500)),
                ('license_no', models.IntegerField(unique=True)),
                ('license_exp_date', models.DateField(help_text='Please use the following format: <em>MM-DD-YYYY</em>.')),
                ('current_station_of_work', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='VetMedicineDistributionData',
            fields=[
                ('entry_no', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField(help_text='Please use the following format: <em>MM-DD-YYYY</em>.')),
                ('product_name', models.CharField(max_length=100)),
                ('opening_balance', models.IntegerField(max_length=20)),
                ('procured_quantity', models.IntegerField(max_length=20)),
                ('procured_batch_no', models.IntegerField(max_length=20, unique=True)),
                ('distributed_quantity', models.IntegerField(max_length=20)),
                ('distributed_batch_no', models.IntegerField(max_length=20, unique=True)),
                ('balance_in_stock', models.IntegerField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='VetMedicineProducer',
            fields=[
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('kvb_reg_no', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('email', models.EmailField(max_length=254)),
                ('academic_inst', models.CharField(max_length=100)),
                ('program_studied', models.CharField(choices=[('CERT', 'Certificate in AH'), ('DIP', 'Diploma in AH'), ('BSC', 'Bachelor of Science in AH'), ('BVM', 'Bachelor of Science in Vetenary Medicine')], max_length=100)),
                ('index_no', models.IntegerField(unique=True)),
                ('year_of_graduation', models.DateField(help_text='Please use the following format: <em>MM-DD-YYYY</em>.')),
                ('academic_cert_reg_no', models.IntegerField(unique=True)),
                ('any_other_certs', models.CharField(max_length=500)),
                ('license_no', models.IntegerField(unique=True)),
                ('license_exp_date', models.DateField(help_text='Please use the following format: <em>MM-DD-YYYY</em>.')),
                ('current_station_of_work', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='VetMedicineProductionData',
            fields=[
                ('entry_no', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField(help_text='Please use the following format: <em>MM-DD-YYYY</em>.')),
                ('product_name', models.CharField(max_length=100)),
                ('opening_balance', models.IntegerField(max_length=20)),
                ('produced_quantity', models.IntegerField(max_length=20)),
                ('produced_batch_no', models.IntegerField(max_length=20, unique=True)),
                ('distributed_quantity', models.IntegerField(max_length=20)),
                ('distributed_batch_no', models.IntegerField(max_length=20, unique=True)),
                ('balance_in_stock', models.IntegerField(max_length=20)),
                ('distributed_to', models.ForeignKey(blank=True, default=0, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='vdh.VetMedicineDistributer')),
            ],
        ),
        migrations.RemoveField(
            model_name='practitioner',
            name='supervising_vet',
        ),
        migrations.AddField(
            model_name='vet',
            name='is_vpp',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='vet',
            name='license_exp_date',
            field=models.DateField(help_text='Please use the following format: <em>MM-DD-YYYY</em>.'),
        ),
        migrations.AlterField(
            model_name='vet',
            name='year_of_graduation',
            field=models.DateField(help_text='Please use the following format: <em>MM-DD-YYYY</em>.'),
        ),
        migrations.DeleteModel(
            name='Practitioner',
        ),
        migrations.AddField(
            model_name='vetmedicinedistributiondata',
            name='distributed_to',
            field=models.ForeignKey(blank=True, default=0, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='vdh.Vet'),
        ),
        migrations.AddField(
            model_name='vetmedicinedistributiondata',
            name='procured_from',
            field=models.ForeignKey(blank=True, default=0, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='vdh.VetMedicineProducer'),
        ),
        migrations.AddField(
            model_name='vet',
            name='supervising_vet',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.DO_NOTHING, to='vdh.SupervisingVet'),
        ),
    ]
