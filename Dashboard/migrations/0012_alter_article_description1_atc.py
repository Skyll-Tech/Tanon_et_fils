# Generated by Django 5.1.3 on 2025-01-20 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dashboard', '0011_rename_description_atc1_article_description1_atc_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='Description1_atc',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
