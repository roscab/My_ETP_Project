# Generated by Django 2.1.2 on 2018-10-27 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0018_auto_20181028_0001'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='group',
            field=models.CharField(choices=[('C/C++', 'C/C++'), ('Backend', 'Backend'), ('Frontend', 'Frontend'), ('Phyton', 'Phyton'), ('QA', 'QA'), ('.NET', '.NET')], default=111111, max_length=200),
            preserve_default=False,
        ),
    ]
