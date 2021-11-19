from django.http.response import HttpResponse
from django.shortcuts import render
from .tasks import GetVideos
from .models import Video
from django.core.paginator import Paginator
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .serializers import VideoItemSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework import generics
from rest_framework.pagination import LimitOffsetPagination

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 1000


def test(request):
    videos = GetVideos.delay()
    print(videos)
    return HttpResponse(200)

class VideoDataViews(APIView, LimitOffsetPagination):
    def get(self, request):
        items = Video.objects.all().order_by('-published_time')
        results = self.paginate_queryset(items, request, view=self)
        serializer = VideoItemSerializer(results, many=True)
        return self.get_paginated_response(serializer.data)

class SearchVideos(generics.ListAPIView):
    serializer_class = VideoItemSerializer
    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        if self.request.method == 'GET':
            title = self.request.GET.get('title', None)
            videos = Video.objects.all().values()
            results = []
            for video in videos:
                if title in video['title'] or title in video['description']:
                    results.append(video)
            return results

    
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