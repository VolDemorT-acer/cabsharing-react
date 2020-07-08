# Generated by Django 3.0.4 on 2020-06-30 05:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Notifications', '0002_auto_20200629_1629'),
    ]

    operations = [
        migrations.RenameField(
            model_name='connectionhistory',
            old_name='last_seen',
            new_name='first_login',
        ),
        migrations.AddField(
            model_name='connectionhistory',
            name='device_id',
            field=models.CharField(blank=True, default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='connectionhistory',
            name='status',
            field=models.CharField(choices=[('online', 'online'), ('offline', 'offline'), ('away', 'away')], default='offline', max_length=10),
        ),
        migrations.AddField(
            model_name='connectionhistory',
            name='user',
            field=models.ForeignKey(blank=True, default='1', on_delete=django.db.models.deletion.CASCADE, related_name='connection', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='connectionhistory',
            name='last_echo',
            field=models.DateTimeField(),
        ),
        migrations.AlterUniqueTogether(
            name='connectionhistory',
            unique_together={('user', 'device_id')},
        ),
        migrations.RemoveField(
            model_name='connectionhistory',
            name='online',
        ),
    ]