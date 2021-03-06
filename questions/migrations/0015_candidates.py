# Generated by Django 2.1.2 on 2018-10-27 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0014_auto_20181016_1730'),
    ]

    operations = [
        migrations.CreateModel(
            name='Candidates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('recruiter', models.CharField(choices=[('Guillermo', 'Guillermo'), ('Vernonica', 'Vernonica')], max_length=200)),
                ('contac_date', models.DateField()),
                ('technical_interview_date', models.DateField()),
                ('level', models.CharField(choices=[('Junior', 'Junior'), ('Profesional', 'Profesional'), ('Senior', 'Senior')], max_length=200)),
                ('bul_interview_date', models.DateField()),
                ('client', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=200)),
                ('next_step', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Candidates',
            },
        ),
    ]
