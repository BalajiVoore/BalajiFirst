# Generated by Django 2.2.5 on 2019-09-19 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imageNew', models.ImageField(upload_to='images')),
                ('summary', models.CharField(max_length=200)),
            ],
        ),
    ]
