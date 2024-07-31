# Generated by Django 4.2.8 on 2024-07-30 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0004_adongsearchhistory_noorisearchhistory_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='SearchResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='category',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='latitude',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='longitude',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='menu',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]