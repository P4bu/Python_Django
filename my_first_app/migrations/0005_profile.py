# Generated by Django 5.1.2 on 2024-10-25 13:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_first_app', '0004_author_book_authors'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('website', models.URLField()),
                ('biography', models.TextField(max_length=300)),
                ('author', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='my_first_app.author')),
            ],
        ),
    ]