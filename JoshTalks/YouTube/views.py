from django.http.response import HttpResponse
from django.shortcuts import render
import argparse
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from rest_framework import viewsets
from rest_framework import permissions
from .tasks import GetVideos


# DEVELOPER_KEY = "AIzaSyBCcsbT4RbpXm7wDmRUaAokQeMarSZNol4"
# YOUTUBE_API_SERVICE_NAME = 'youtube'
# YOUTUBE_API_VERSION = 'v3'
# PREDEFINED_QUERY = "Fashion"

# async def GetVideos(Request):
#     youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)

#     search_response = youtube.search().list(
#         q=PREDEFINED_QUERY,
#         part='id,snippet',
#         maxResults=25,
#         type='video'
#     ).execute()

#     videos = []

#     for search_result in search_response.get('items', []):
#         print(search_result['id'])
#         videos.append((search_result['id']['videoId'], search_result['snippet']))

#     return HttpResponse(videos)

def test(request):
    GetVideos.delay()
    return HttpResponse(200)


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