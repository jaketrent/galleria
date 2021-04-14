# Generated by Django 3.2 on 2021-04-13 12:26

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccessToken',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('expires', models.DateTimeField(blank=True, null=True)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
    ]
