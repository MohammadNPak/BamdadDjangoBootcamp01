# Generated by Django 4.1.7 on 2023-03-01 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialnetwork', '0004_user_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_picture',
            field=models.ImageField(default='profile_pictures\\default_profile_picture.png', upload_to='profile_pictures'),
        ),
    ]
