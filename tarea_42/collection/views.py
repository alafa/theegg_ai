from django.shortcuts import render
from collection.models import VideoItem


# Create your views here.
def home(request):
    video_items = VideoItem.objects.all()
    return render(request, 'collection/home.html', {"video_items": video_items})


def about(request):
    return render(request, 'collection/about.html')


def video(request, pk):
    item = VideoItem.objects.get(pk=pk)
    return render(request, 'collection/video.html', {"video_item": item})
