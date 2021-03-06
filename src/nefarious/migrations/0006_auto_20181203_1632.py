# Generated by Django 2.1.1 on 2018-12-03 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nefarious', '0005_nefarioussettings_quality_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='watchmovie',
            name='quality_profile',
            field=models.CharField(blank=True, choices=[('any', 'any'), ('sd', 'sd'), ('hd-720p', 'hd-720p'), ('hd-1080p', 'hd-1080p'), ('ultra-hd', 'ultra-hd'), ('hd-720p-1080p', 'hd-720p-1080p')], max_length=500),
        ),
        migrations.AddField(
            model_name='watchtvepisode',
            name='quality_profile',
            field=models.CharField(blank=True, choices=[('any', 'any'), ('sd', 'sd'), ('hd-720p', 'hd-720p'), ('hd-1080p', 'hd-1080p'), ('ultra-hd', 'ultra-hd'), ('hd-720p-1080p', 'hd-720p-1080p')], max_length=500),
        ),
        migrations.AddField(
            model_name='watchtvshow',
            name='quality_profile',
            field=models.CharField(blank=True, choices=[('any', 'any'), ('sd', 'sd'), ('hd-720p', 'hd-720p'), ('hd-1080p', 'hd-1080p'), ('ultra-hd', 'ultra-hd'), ('hd-720p-1080p', 'hd-720p-1080p')], max_length=500),
        ),
        migrations.AlterField(
            model_name='nefarioussettings',
            name='quality_profile',
            field=models.CharField(choices=[('any', 'any'), ('sd', 'sd'), ('hd-720p', 'hd-720p'), ('hd-1080p', 'hd-1080p'), ('ultra-hd', 'ultra-hd'), ('hd-720p-1080p', 'hd-720p-1080p')], default='hd-720p-1080p', max_length=500),
        ),
    ]
