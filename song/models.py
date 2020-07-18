from django.db import models

# Create your models here.
from singer.models import Singer

class Album(models.Model):
    # singer_id = models.IntegerField('歌手id', db_index=True)
    # # TODO 是否需要?
    # singer_name = models.CharField('歌手', max_length=30)
    singer = models.ForeignKey(Singer, on_delete=models.CASCADE)
    album_name = models.CharField('专辑名', max_length=30)
    album_pic_path = models.CharField('专辑封面', max_length=45)
    is_active = models.BooleanField('授权', default=0)

    class Meta:
        db_table = 'song_album'

class Song(models.Model):
    name = models.CharField('歌曲名称', max_length=16)
    # 点击量
    ctr = models.IntegerField('点击量', default=0)
    # TODO 是否需要
    # singer_name = models.CharField('歌手', max_length=30, default='')
    # singer_id = models.IntegerField('歌手id', db_index=True)
    singer = models.ForeignKey(Singer, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, null=True)
    # '[流行，运动，粤语]'--->'101'
    lable_set = models.IntegerField('标签', default=0)
    is_active = models.BooleanField('授权', default=0)
    duration =models.IntegerField('时长',default=1)
    def __str__(self):
        return '歌曲：' + self.name

    class Meta:
        db_table = 'song_song'
        verbose_name_plural = '曲库'


class SongPath(models.Model):
    id = models.IntegerField('id', primary_key=True)
    song_path = models.CharField('url', max_length=255)
    song_pic_path = models.CharField('图片路劲', max_length=45)

    class Meta:
        db_table = 'song_song_path'

class Lyric(models.Model):
    song_lyric = models.TextField('歌词', default='')
    song = models.OneToOneField(Song, on_delete=models.CASCADE)
