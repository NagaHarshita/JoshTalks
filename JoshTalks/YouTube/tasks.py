from celery import shared_task
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from rest_framework import viewsets
from rest_framework import permissions
from .models import Video


DEVELOPER_KEY = "AIzaSyBCcsbT4RbpXm7wDmRUaAokQeMarSZNol4"
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'
PREDEFINED_QUERY = "Travel"

def DeleteAll():
    Video.objects.all().delete()

@shared_task(bind=True)
def GetVideos(self):

    DeleteAll()

    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)

    search_response = youtube.search().list(
        q=PREDEFINED_QUERY,
        part='id,snippet',
        maxResults=200,
        type='video',
        order='date',
        publishedAfter='2021-1-1T00:00:00.0Z'
    ).execute()

    videos = []

    for search_result in search_response.get('items', []):
        print(search_result['id'])
        videos.append(search_result['id']['videoId'])
        Video.objects.create(
            video_id = search_result['id']['videoId'], 
            title = search_result['snippet']['title'],
            description = search_result['snippet']['description'],
            channel_id = search_result['snippet']['channelId'],
            channel_title = search_result['snippet']['channelTitle'],
            published_time = search_result['snippet']['publishTime']
        )
        print(len(videos))

    return videos