# Generated by Django 4.2.9 on 2024-01-18 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_post_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to='blog/'),
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.ManyToManyField(to='blog.category'),
        ),
    ]
