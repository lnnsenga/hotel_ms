# Generated by Django 4.2.7 on 2023-11-16 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0003_alter_user_avatar_url_alter_user_email_verified'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar_url',
            field=models.ImageField(upload_to='media/'),
        ),
    ]
