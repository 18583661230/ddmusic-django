from django.db import models
import random

GENDER=((0,'男'),(1,'女'),(2,'保密'))
# Create your models here.
class User(models.Model):
    # 字段不为空,用户名在数据库唯一
    username = models.CharField('用户名', max_length=32, blank=False, unique=True)
    password = models.CharField('密码', max_length=32, blank=False)

    class Meta:
        db_table = 'user'


def default_sign():
    sign = ['人生到老不容易，不能事事都如意。',
            '一杯苦酒对月歌，歌不尽离愁，明月清风与谁说，说不出寂寞。',
            '快乐不像烦恼那样随时随地的跟随在你的身边。',
            '你在飞奔，我在行走！可我，永远不会摔倒。',
            '时光不老、我们依旧还在。',
            '时间在背后，它看不见我的脸，我躲不开它。']
    return random.choice(sign)


def default_info():
    info = []
    return random.choice(info)


class UserInfo(models.Model):
    # uid 主键,必填
    # email 允许为空,且唯一存在
    # 性别 bool型
    # age 默认18
    # 职业 默认 未填写
    # 用户头像 avatar内存储
    # 个人签名 default_sing列表内随机获取
    # 个人描述 默认添加
    # 创建时间 第一次创建自动设置
    # 更新时间 保存对象自动设置
    # 电话号码11位,唯一存在
    uid = models.CharField('用户id', primary_key=True, max_length=8, blank=False)
    email = models.EmailField('邮箱', max_length=255, null=True, unique=True)
    gender = models.CharField('性别',max_length=2, choices=GENDER)
    age = models.CharField('年龄', max_length=8, default=18)
    career = models.CharField('职业', max_length=45, default='未填写')
    salary_range = models.CharField('工资范围', max_length=45, default='未填写')
    avatar_id = models.ImageField('用户头像', upload_to='avatar', null=True)
    sign = models.CharField('个人签名', max_length=255, default=default_sign)
    info = models.CharField('个人描述', max_length=255, default='这家伙很懒,什么也没留下...')
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    updated_time = models.DateTimeField('更新时间', auto_now=True)
    # 新增字段
    phone = models.CharField('电话号码', max_length=11, unique=True)

    class Meta:
        db_table = 'user_info'


class UserFollow():
    # 关注类型,默认为空长度255
    uid = models.CharField('用户id', primary_key=True, max_length=8, blank=False)
    lable_set = models.CharField('关注类型', max_length=255, default='')

    class Meta:
        db_table = 'user_follow'
