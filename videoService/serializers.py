from rest_framework import serializers
from videoService.models import Video
from moviepy.editor import VideoFileClip
from vuploader.settings import BASE_DIR
import os

class VideoSerializer(serializers.ModelSerializer):
    def validate_video(self,value): 
        if value.size > 859832320: 
            raise serializers.ValidationError("video excedes 10 gb of file size")
        if not value.name.split(".")[-1] in ["mp4","mkv"] :
            raise serializers.ValidationError("extension invalid")
        if (length:=self.check_length_file(value)) > 600:
            raise serializers.ValidationError("video excedes 10 min margin")
        self.initial_data["length"]=int(length)
        self.initial_data["size"]=value.size
        return value


    def check_length_file(self,f):
        name=f'temp/{f.name}'
        with open(name, 'wb+') as destination:
            for chunk in f.chunks():
                destination.write(chunk)
        clip=VideoFileClip(name)
        duration=clip.duration
        clip.close()
        os.remove(BASE_DIR/name)
        return duration


    class Meta:
        model=Video
        fields=["title","video","length","size","type","created_at"]
        read_only_fields=["created_at","length","size"]
        



