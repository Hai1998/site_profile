# Generated by Django 4.0.6 on 2022-07-28 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Commercials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_text', models.CharField(max_length=15)),
                ('second_text', models.CharField(max_length=50)),
                ('thirst_text', models.CharField(max_length=50)),
                ('image_name', models.CharField(max_length=100)),
                ('commercials_image', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
