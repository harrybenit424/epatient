# Generated by Django 2.1.5 on 2019-02-03 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='', max_length=200, unique=True)),
                ('last_name', models.CharField(default='', max_length=200, unique=True)),
                ('birthday', models.DateField(null=True)),
                ('gender', models.BooleanField(default=True)),
                ('postcode', models.CharField(default='', max_length=100)),
                ('address', models.CharField(default='', max_length=254)),
                ('useremail', models.EmailField(default='', max_length=254, unique=True)),
                ('password', models.CharField(default='', max_length=200)),
                ('user_type', models.CharField(choices=[('AD', 'Administrator'), ('MD', 'medical'), ('PA', 'patient')], default='PA', max_length=2)),
                ('phone_number', models.CharField(default='', max_length=200, unique=True)),
                ('verify_code', models.CharField(max_length=10, null=True)),
                ('verify_time', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=False)),
            ],
        ),
    ]
