# Generated by Django 4.2.5 on 2024-02-29 16:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0002_alter_organization_website'),
    ]

    operations = [
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=100)),
                ('company', models.CharField()),
                ('description', models.TextField()),
                ('tech_stack', models.JSONField(default=list)),
                ('start_month', models.CharField()),
                ('start_year', models.PositiveSmallIntegerField()),
                ('end_month', models.CharField(blank=True, null=True)),
                ('end_year', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('job_seeker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='experience', to='accounts.jobseeker')),
            ],
        ),
    ]
