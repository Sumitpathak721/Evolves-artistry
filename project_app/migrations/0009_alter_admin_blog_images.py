# Generated by Django 4.0.6 on 2022-08-03 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_app', '0008_alter_admin_blog_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin_blog',
            name='images',
            field=models.ImageField(upload_to='./static/blog'),
        ),
    ]
