# Generated by Django 4.0.3 on 2022-03-13 10:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('institutes', '0005_delete_projects'),
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(default='', max_length=250)),
                ('department', models.CharField(default='', max_length=60)),
                ('tags', models.CharField(default='', max_length=200)),
                ('description', models.TextField()),
                ('thumbnail', models.ImageField(upload_to='Projects/')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
