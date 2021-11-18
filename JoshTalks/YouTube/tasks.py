from celery import shared_task
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from rest_framework import viewsets
from rest_framework import permissions


DEVELOPER_KEY = "AIzaSyBCcsbT4RbpXm7wDmRUaAokQeMarSZNol4"
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'
PREDEFINED_QUERY = "Fashion"


@shared_task(bind=True)
def GetVideos(self):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)

    search_response = youtube.search().list(
        q=PREDEFINED_QUERY,
        part='id,snippet',
        maxResults=25,
        type='video'
    ).execute()

    videos = []

    for search_result in search_response.get('items', []):
        print(search_result['id'])
        videos.append((search_result['id']['videoId'], search_result['snippet']))

    return videos