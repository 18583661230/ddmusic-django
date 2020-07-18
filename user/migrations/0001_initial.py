# Generated by Django 2.2.12 on 2020-07-09 08:12

from django.db import migrations, models
import user.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=32, unique=True, verbose_name='用户名')),
                ('password', models.CharField(max_length=32, verbose_name='密码')),
            ],
            options={
                'db_table': 'user',
            },
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('uid', models.CharField(max_length=8, primary_key=True, serialize=False, verbose_name='用户id')),
                ('email', models.EmailField(max_length=255, null=True, unique=True, verbose_name='邮箱')),
                ('gender', models.CharField(choices=[(0, '男'), (1, '女'), (2, '保密')], max_length=2, verbose_name='性别')),
                ('age', models.CharField(default=18, max_length=8, verbose_name='年龄')),
                ('career', models.CharField(default='未填写', max_length=45, verbose_name='职业')),
                ('salary_range', models.CharField(default='未填写', max_length=45, verbose_name='工资范围')),
                ('avatar_id', models.ImageField(null=True, upload_to='avatar', verbose_name='用户头像')),
                ('sign', models.CharField(default=user.models.default_sign, max_length=255, verbose_name='个人签名')),
                ('info', models.CharField(default='这家伙很懒,什么也没留下...', max_length=255, verbose_name='个人描述')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('phone', models.CharField(max_length=11, unique=True, verbose_name='电话号码')),
            ],
            options={
                'db_table': 'user_info',
            },
        ),
    ]