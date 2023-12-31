# Generated by Django 4.2.6 on 2023-10-06 09:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BranchSetup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch_name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=300)),
                ('create_date', models.DateField(auto_now_add=True)),
                ('update_date', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='StaffUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(max_length=100)),
                ('address', models.TextField()),
                ('create_date', models.DateField(auto_now_add=True, null=True)),
                ('update_date', models.DateField(auto_now=True)),
                ('admin', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('branch_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminstrator_app.branchsetup')),
            ],
        ),
    ]
