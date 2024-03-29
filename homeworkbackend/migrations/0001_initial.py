# Generated by Django 2.2.6 on 2019-11-11 15:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Soldier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.TextField()),
                ('last_name', models.TextField()),
                ('date_of_birth', models.DateField()),
                ('arm_of_service', models.CharField(choices=[('A', 'Air Force'), ('N', 'Navy'), ('G', 'Ground Force')], max_length=1, null=True)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homeworkbackend.Country')),
            ],
        ),
    ]
