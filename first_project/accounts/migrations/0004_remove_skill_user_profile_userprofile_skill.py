# Generated by Django 4.1.7 on 2023-03-15 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_rename_profassional_status_userprofile_professional_status_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='skill',
            name='user_profile',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='skill',
            field=models.ManyToManyField(to='accounts.skill'),
        ),
    ]
