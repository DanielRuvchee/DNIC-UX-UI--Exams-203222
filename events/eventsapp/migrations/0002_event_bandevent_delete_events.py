# Generated by Django 5.0.6 on 2024-06-28 20:46

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventsapp', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=244)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('poster', models.ImageField(blank=True, null=True, upload_to='event_images')),
                ('bands', models.CharField(blank=True, max_length=255, null=True)),
                ('info', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BandEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('band', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eventsapp.bands')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eventsapp.event')),
            ],
        ),
        migrations.DeleteModel(
            name='Events',
        ),
    ]