# Generated by Django 4.2.11 on 2024-06-28 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_usergroup_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='chat_id',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Чат id'),
        ),
    ]