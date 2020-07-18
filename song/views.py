from django.http import JsonResponse
from django.shortcuts import render
from django.core.cache import cache
from .models import *
from django_redis import get_redis_connection
from django.conf import settings
from tools.play_music_cache import cache_song_dec


# 错误码 10500-10599

# Create your views here.

@cache_song_dec(60)
def play_view(request):
    if request.method == 'GET':
        song_id = request.GET.get('id')
        try:
            song = Song.objects.get(id=song_id, is_active=1)
            song_path = SongPath.objects.get(id=song_id)
        except Exception as e:
            res = {'code': 10502, 'error': 'no song'}
            return JsonResponse(res)
        data = {
            'song_name': song.name,
            'singer_name': song.singer_name,
            'singer_id': song.singer_id,
            'song_path': song_path.song_path
        }
        if song.lyric_id:
            data['lyric_id'] = song.lyric_id
        if song.album_id:
            album = Album.objects.get(id=song.album_id)
            # TODO 路径更正
            # album_pic_path = album.album_pic_path
            data['album_id'] = album.id
            data['album_name'] = album.album_name
            data['album_pic_path'] = album.album_pic_path
        else:
            data['song_pic_path'] = song_path.song_pic_path
        res = {'code': 200, 'data': data}
        return JsonResponse(res)


def rank_view(request):
    if request.method == 'GET':
        # 判断是否有query
        order_by = request.GET.get('order_by')
        if not order_by:
            key = 'ranking_list'
            rank_list = cache.get(key)
            if not rank_list:
                # rank_list = Song.objects.order_by('-')
                pass
        res = {'code': 200, 'data': 'data'}
        return JsonResponse(res)
