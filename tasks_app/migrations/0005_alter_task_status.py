# Generated by Django 4.2.11 on 2024-06-12 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks_app', '0004_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('to_do', 'To Do'), ('in_progress', 'In Progress'), ('done', 'Done'), ('in_progress_ex_prod', 'In Progress Ex Prod'), ('done_ex_prod', 'Done Ex Prod')], default='to_do', max_length=20),
        ),
    ]
