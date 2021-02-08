from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse

def index(request):
    if request.method == 'POST':
        return render(request, 'simple_upload.html', {
            'uploaded_file_url': '123',
        })

    return render(request, 'simple_upload.html')

def ok(request):
    return HttpResponse("Server is ok.")