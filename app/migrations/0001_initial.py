# Generated by Django 3.1.7 on 2021-03-08 12:00

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=222, null=True)),
                ('content', tinymce.models.HTMLField()),
            ],
        ),
    ]