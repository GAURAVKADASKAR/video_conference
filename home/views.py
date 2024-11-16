from django.shortcuts import render


def welcome(request):
    return render(request,'index.html')

def video_call(request):
    return render(request,'video.html')
