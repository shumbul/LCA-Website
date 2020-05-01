# Generated by Django 3.0.5 on 2020-04-29 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ngo',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('reg_number', models.CharField(max_length=25, primary_key=True, serialize=False)),
                ('category', models.IntegerField(choices=[(0, 0), (1, 1)], default=0)),
                ('address', models.CharField(max_length=255)),
                ('contact_number', models.CharField(max_length=10)),
                ('email_address', models.CharField(max_length=255)),
                ('website', models.CharField(max_length=75, null=True)),
                ('approved', models.BooleanField(default=False)),
            ],
        ),
    ]