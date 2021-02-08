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


def add(request):
    a = int(request.GET.get('a', 0))
    b = int(request.GET.get('b', 0))
    result = a + b

    return HttpResponse(str(result))
