from django.http.response import HttpResponse
from django.shortcuts import render
import argparse
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from rest_framework import viewsets
from rest_framework import permissions

# Create your views here.

DEVELOPER_KEY = "AIzaSyBCcsbT4RbpXm7wDmRUaAokQeMarSZNol4"
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'

async def youtube_search(options):
    
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
        developerKey=DEVELOPER_KEY)

    search_response = youtube.search().list(
        q="Google",
        part='id,snippet',
        maxResults=25
    ).execute()

    videos = []

    for search_result in search_response.get('items', []):

        if search_result['id']['kind'] == 'youtube#video':
            videos.append('%s (%s)' % (search_result['snippet']['title'],
                                    search_result['id']['videoId']))

    print ('Videos:\n', '\n'.join(videos), '\n')
    return HttpResponse(200)