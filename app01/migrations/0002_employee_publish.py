# Generated by Django 4.1.2 on 2022-11-18 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='publish',
            field=models.CharField(default='人民出版社', max_length=12, null=True),
        ),
    ]