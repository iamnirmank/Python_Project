from rest_framework import viewsets,status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from videoService.serializers import VideoSerializer
from videoService.models import Video
from rest_framework.views import APIView


SIZE_THRESHOLD=500
LENGTH_THRESHOLD=378

class VideoView(viewsets.ModelViewSet):
    serializer_class = VideoSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        videos=Video.objects.all()
        if(date := self.request.query_params.get("date")):
            videos=videos.filter(created_at=date)
        if(length := self.request.query_params.get("less_than_time")):
            videos=videos.filter(length__lte=length)
        if(type := self.request.query_params.get("type")):
            videos=videos.filter(type=type)
        return videos
        
        
           

    def post(self,request):
        serializer=VideoSerializer(data=request.data)
        if not serializer.is_valid():
              return Response(
                {"status":status.HTTP_400_BAD_REQUEST,"message":serializer.errors}
            )
            
        video=serializer.save(length=serializer.initial_data["length"],size=serializer.initial_data["size"])
        return Response(
                {"status":status.HTTP_201_CREATED,"message":"successfully created a video","id":video.id}
            )
    
    def list(self,request,*args,**kwargs):
        
        return super().list(request,*args,**kwargs)

    


class VideoCheckView(APIView):
    def get(self,request):
        length=int(request.query_params.get("length")) #in secs
        type=request.query_params.get("type")
        size=int(request.query_params.get("size")) #in mb
        cost= 5 if size<SIZE_THRESHOLD else 12.5
        cost+= 12.5 if length<LENGTH_THRESHOLD else 20
        return Response(
                {"status":status.HTTP_200_OK,"cost":cost}
            )
        




