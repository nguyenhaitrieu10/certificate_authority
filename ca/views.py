from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage

import sys
fs = FileSystemStorage()

def index(request):
    if request.method == 'POST':
        return render(request, 'simple_upload.html', {
            'uploaded_file_url': '123',
        })

    return render(request, 'simple_upload.html')
