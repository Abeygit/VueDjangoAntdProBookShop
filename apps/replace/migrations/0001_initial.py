# Generated by Django 3.1.1 on 2020-10-09 22:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VersionControl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version_code', models.CharField(blank=True, max_length=10, null=True, verbose_name='版本号')),
                ('file', models.FileField(blank=True, help_text='前端js文件', null=True, upload_to='message/images/', verbose_name='前端js文件')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '版本信息',
                'verbose_name_plural': '版本信息',
                'db_table': 'replace_version',
            },
        ),
    ]
