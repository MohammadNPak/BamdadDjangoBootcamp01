# Generated by Django 4.1.7 on 2023-04-08 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_alter_userprofile_github_username'),
        ('socialnetwork', '0008_post_dislike_post_like'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='dislike',
            field=models.ManyToManyField(blank=True, null=True, related_name='dislike_set', to='accounts.userprofile'),
        ),
        migrations.AlterField(
            model_name='post',
            name='like',
            field=models.ManyToManyField(blank=True, null=True, related_name='like_set', to='accounts.userprofile'),
        ),
    ]
