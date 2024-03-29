# Generated by Django 5.0.2 on 2024-02-15 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_alter_project_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutMe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('experience', models.TextField()),
                ('image', models.ImageField(upload_to='about_me/')),
                ('projects', models.ManyToManyField(to='portfolio.project')),
            ],
        ),
    ]
