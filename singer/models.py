from django.db import models
import random

# Create your models here.
from user.models import User

GENDER=(('0','男'),('1','女'),('2','保密'))
AREAS=((('0','中国'),('1','欧美'),('2','日韩'),('3','其他')))
class Singer(models.Model):
    id = models.IntegerField('ID', primary_key=True)
    # 歌手名
    name = models.CharField('名称', max_length=32, blank=False)
    # 歌手标签 用序列字符串表示
    lable_set = models.CharField('标签', max_length=50,blank=True)
    area = models.CharField('地区', max_length=2, choices=AREAS,default='0')
    is_team = models.BooleanField('乐队', default=False)
    introduce = models.CharField('简介', max_length=150,blank=True)

    class Meta:
        db_table = 'singer'


class SingerInfo(models.Model):
    # 性别 bool型
    # age 默认18
    # 用户头像 avatar内存储
    # 个人描述 默认添加
    # 创建时间 第一次创建自动设置
    # 更新时间 保存对象自动设置
    name = models.CharField('姓名', max_length=32, blank=False,default='')
    country = models.CharField('国籍', max_length=30)
    # email = models.EmailField('邮箱', max_length=255, null=True, unique=True)
    gender = models.CharField('性别',max_length=2, choices=GENDER)
    age = models.CharField('年龄', max_length=8, null=True)
    # career = models.CharField('职业', max_length=45, default='未填写')
    # salary_range = models.CharField('工资范围', max_length=45, default='未填写')
    avatar = models.ImageField('头像', upload_to='avatar', blank=True)
    # sign = models.CharField('个人签名', max_length=255, default=default_sign)
    info = models.CharField('歌手介绍', max_length=255, blank=True)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    updated_time = models.DateTimeField('更新时间', auto_now=True)
    singer = models.ForeignKey(Singer, on_delete=models.CASCADE)

    class Meta:
        db_table = 'singer_info'


class UserFollow():
    uid = models.ForeignKey(User, on_delete=models.CASCADE)
    sid = models.ForeignKey(Singer, on_delete=models.CASCADE)

    class Meta:
        db_table = 'user_follow'
