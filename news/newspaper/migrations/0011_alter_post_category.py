# Generated by Django 4.1.3 on 2022-11-29 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newspaper', '0010_alter_post_category_alter_post_title_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(default='news', max_length=255),
        ),
    ]
