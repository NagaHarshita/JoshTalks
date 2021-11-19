from celery import shared_task
from googleapiclient.discovery import build
from .models import Video


DEVELOPER_KEY = "AIzaSyDUlOxGZ5WZZ-2poZfIaVjQRGNLnh_uJsI"
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'
PREDEFINED_QUERY = "Music"

def DeleteAll():
    Video.objects.all().delete()


def LoadPaginatedResults(youtube, nextToken):
    search_response = youtube.search().list(
        q=PREDEFINED_QUERY,
        part='id,snippet',
        pageToken = nextToken,
        type='video',
        order='date',
        publishedAfter='2020-1-1T00:00:00.0Z'
    ).execute()

    return search_response

def CollectData(search_response):
    videoIds = []
    for search_result in search_response.get('items', []):
        videoIds.append(search_result['id']['videoId'])
        Video.objects.create(
            video_id = search_result['id']['videoId'], 
            title = search_result['snippet']['title'],
            description = search_result['snippet']['description'],
            channel_id = search_result['snippet']['channelId'],
            channel_title = search_result['snippet']['channelTitle'],
            published_time = search_result['snippet']['publishTime']
        )

    return videoIds

@shared_task(bind=True)
def GetVideos(self):
    DeleteAll()
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)
    videoIds = []
    
    nextPageToken = None 
    i=0
    while i<3:
        page = LoadPaginatedResults(youtube, nextPageToken)
        videoIds.extend(CollectData(page))
        nextPageToken = page.get("nextPageToken")
        if not nextPageToken:
            break
        i+=1


    return videoIds
