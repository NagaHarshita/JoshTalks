from django.http.response import HttpResponse
from django.shortcuts import render
from .tasks import GetVideos
from .models import Video
from django.core.paginator import Paginator
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def test(request):
    videos = GetVideos.delay()
    print(videos)
    return HttpResponse(200)
    
def fetchData(request):
    videoData = Video.objects.all().order_by('-published_time')
    page = request.GET.get('page', 1)

    paginator = Paginator(videoData, 10)
    try:
        videos = paginator.page(page)
    except PageNotAnInteger:
        videos = paginator.page(1)
    except EmptyPage:
        videos = paginator.page(paginator.num_pages)

    return render(request, 'videos.html', { 'videos': videos })

def searchByTitle(request):
    param = request.name
    videoData = Video.objects.all()
    for i in videoData:
        if videoData['title'] == param:
            return HttpResponse(200)
    return HttpResponse(404)

def searchByDesc(request):
    param = request.name
    videoData = Video.objects.all()
    for i in videoData:
        if videoData['description'] == param:
            return HttpResponse(200)
    return HttpResponse(404)


    # Schema of the returned JSON
    # {
    #     'publishedAt': '2021-11-18T06:10:21Z', 
    #     'channelId': 'UCoVwq0vh-XD8RrEyDZ0KeJw', 
    #     'title': '#GoogleForIndia 2021', 
    #     'description': "The internet's impact - in our personal lives, on businesses, and our institutions - has been profound and pervasive. At this 7th edition of our annual Google for ...", 
    #     'thumbnails': {
    #         'default': {
    #             'url': 'https://i.ytimg.com/vi/h-jZQaiCmps/default.jpg', 
    #             'width': 120, 
    #             'height': 90
    #         }, 
    #         'medium': {
    #             'url': 'https://i.ytimg.com/vi/h-jZQaiCmps/mqdefault.jpg', 
    #             'width': 320, 
    #             'height': 180
    #         }, 
    #         'high': {
    #             'url': 'https://i.ytimg.com/vi/h-jZQaiCmps/hqdefault.jpg', 
    #             'width': 480, 
    #             'height': 360
    #         }
    #     }, 
    #     'channelTitle': 'Google India', 
    #     'liveBroadcastContent': 'none', 
    #     'publishTime': '2021-11-18T06:10:21Z'
    # }
