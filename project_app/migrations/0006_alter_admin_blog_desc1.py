# Generated by Django 4.0.6 on 2022-08-02 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_app', '0005_rename_image_admin_blog_images_admin_blog_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin_blog',
            name='desc1',
            field=models.TextField(default=''),
        ),
    ]
