from django.http import JsonResponse
from django.core.cache import cache
from song.models import *
from django_redis import get_redis_connection
from django.conf import settings


def cache_song_dec(expire):
    def _cache_song_dec(func):
        def wrapper(request, *args, **kwargs):
            r = get_redis_connection()
            song_id = request.GET.get('id')
            if not song_id:
                res = {'code': 10501, 'error': 'No id'}
                return JsonResponse(res)
            song_cache_key = 'song_data_by_id:%s' % song_id
            if cache.get(song_cache_key):
                print('----return cache----')
                return cache.get(song_cache_key)

            response = func(request, *args, **kwargs)
            cache.set(song_cache_key, response, expire)
            # TODO 点击量+1
            r.zincrby(settings.REDIS_SONG_CTR_KEY, 1, song_id)
            print('---set cache---')
            return response

        return wrapper

    return _cache_song_dec
