# Generated by Django 3.2.16 on 2024-03-15 12:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20240315_1621'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShortURLList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('shortened_url', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.shortenedurl')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
