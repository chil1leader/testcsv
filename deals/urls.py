from .views import FileUploadAPIView, MemberListAPIView
from django.urls import path

urlpatterns = [
    path('upload/', FileUploadAPIView.as_view()),
    path('list/', MemberListAPIView.as_view()),
]