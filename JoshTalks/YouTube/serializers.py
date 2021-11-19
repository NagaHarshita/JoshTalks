from rest_framework import serializers

from .models import Video

class VideoItemSerializer(serializers.ModelSerializer):
    video_id = serializers.CharField(max_length=30)
    title = serializers.CharField(max_length=30)
    description = serializers.CharField(max_length=250)
    channel_id = serializers.CharField(max_length=30)
    channel_title = serializers.CharField(max_length=30)
    published_time = serializers.DateTimeField()

    class Meta:
        model = Video
        fields = ('__all__')
