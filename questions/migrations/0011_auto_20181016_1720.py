# Generated by Django 2.1.2 on 2018-10-16 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0010_auto_20181016_1506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='level',
            field=models.CharField(choices=[('Low', 'Junior'), ('Medium', 'Profesional'), ('High', 'Senior'), ('Not applicable', 'N/A')], max_length=200),
        ),
    ]
