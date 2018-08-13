# Generated by Django 2.0.7 on 2018-08-03 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_course_course_org'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='learn_time',
            new_name='learn_times',
        ),
        migrations.AddField(
            model_name='course',
            name='category',
            field=models.CharField(default='课程类别', max_length=30, verbose_name='课程类别'),
        ),
    ]