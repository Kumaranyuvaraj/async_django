from django.http import HttpResponse
import time,asyncio
from movies.models import Movies
from stories.models import Story
from asgiref.sync import sync_to_async

# helper funcs

def get_movie():
    print("prepare to get the movies...")
    time.sleep(2)
    queryset = Movies.objects.all()
    print(queryset)
    print("got all the movies!")
    
def get_story():
    print("prepare to get the stories...")
    time.sleep(2)
    queryset = Story.objects.all()
    print(queryset)
    print("got all the stories!")
    
@sync_to_async
def get_movie_async():
    print("prepare to get the movies...")
    time.sleep(2)
    queryset = Movies.objects.all()
    print(queryset)
    print("got all the movies!")
 
@sync_to_async   
def get_story_async():
    print("prepare to get the stories...")
    time.sleep(2)
    queryset = Story.objects.all()
    print(queryset)
    print("got all the stories!")




#views

def home_view(request):
    return HttpResponse('Homepage')

def main_view(request):
    start_time = time.time()
    get_movie()
    get_story()
    total = (time.time() - start_time)
    print('total:',total)
    return HttpResponse('sync')

async def main_view_async(request):
    start_time = time.time()
    # task1 = asyncio.ensure_future(get_movie_async())
    # task2 = asyncio.ensure_future(get_story_async())
    # await asyncio.wait([task1,task2])
    await asyncio.gather(get_movie_async(),get_story_async())
    total = (time.time() - start_time)
    print('total:',total)
    return HttpResponse('async')

    # total: 7.026497840881348