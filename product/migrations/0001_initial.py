# Generated by Django 3.2.9 on 2022-02-04 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='productmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pname', models.CharField(max_length=50)),
                ('pdesc', models.CharField(max_length=100)),
                ('pprice', models.IntegerField()),
                ('discount', models.IntegerField()),
                ('pimg', models.ImageField(upload_to='product/')),
            ],
        ),
    ]
