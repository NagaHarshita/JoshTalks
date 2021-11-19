from django.http.response import HttpResponse
from django.shortcuts import render
from .tasks import GetVideos
from .models import Video
from django.core.paginator import Paginator
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .serializers import VideoItemSerializer
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.pagination import LimitOffsetPagination

# testing celery
def test(request):
    videos = GetVideos.delay()
    print(videos)
    return HttpResponse(200)

# GET API that returns all the video-data in the descending order of published-time with pagination
class VideoDataViews(APIView, LimitOffsetPagination):
    def get(self, request):
        try:
            items = Video.objects.all().order_by('-published_time')
            results = self.paginate_queryset(items, request, view=self)
            serializer = VideoItemSerializer(results, many=True)
            return self.get_paginated_response(serializer.data)
        except:
            return []

# SEARCH API that returns video-data whose either title or description contains the query string
class SearchVideos(generics.ListAPIView):
    serializer_class = VideoItemSerializer
    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        if self.request.method == 'GET':
            try:
                query = self.request.GET.get('query', None)
                videos = Video.objects.all().values()
                results = []
                for video in videos:
                    if query in video['title'] or query in video['description']:
                        results.append(video)
                return results
            except:
                return []

# Used to fetch all the video-data in the descending order of published-time with pagination
# Used in the ui
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