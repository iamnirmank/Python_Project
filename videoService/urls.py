from django.urls import path
from videoService.views import VideoView,VideoCheckView

urlpatterns = [
    path("create",VideoView.as_view({"post": "post"}), name="upload_video"),
    path("list",VideoView.as_view({"get": "list"}), name="list_video"),
    path("check",VideoCheckView.as_view(), name="check_cost"),




]