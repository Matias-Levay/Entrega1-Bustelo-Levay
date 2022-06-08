# Generated by Django 4.0.5 on 2022-06-08 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0002_encuestamodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactenosModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=150)),
                ('asunto', models.CharField(max_length=200)),
                ('mensaje', models.TextField()),
                ('fecha', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
